import requests
import pandas as pd
import numpy as np
import requests_cache
from retry_requests import retry
import logging
from typing import Optional, List, Dict, Tuple
from datetime import datetime, timedelta
import json
from urllib.parse import urlparse, parse_qs
import re
import os

# Временной ряд
# https://open-meteo.com/
# https://open-meteo.com/en/docs?hourly=temperature_2m,wind_speed_10m,wind_speed_80m,wind_speed_120m,wind_speed_180m,wind_direction_10m,wind_direction_80m,wind_direction_180m,wind_gusts_10m,wind_direction_120m,precipitation,relative_humidity_2m,weather_code,snowfall,snow_depth,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,rain,showers,vapour_pressure_deficit,apparent_temperature,dew_point_2m&timezone=Europe%2FMoscow&latitude=55.7522&longitude=#hourly_weather_variables

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('storm_warning_system.log', encoding='utf-8'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

# Настройка кэширования и повторных попыток
cache_session = requests_cache.CachedSession('.cache', expire_after=86400)  # 1 день
retry_session = retry(cache_session, retries=5, backoff_factor=0.3)


def parse_parameters_from_url(url: str) -> Tuple[Optional[float], Optional[float], List[str], Optional[str]]:
    try:
        parsed = urlparse(url)
        query = parse_qs(parsed.query)

        latitude = float(query.get('latitude', [None])[0]) if query.get('latitude') else None
        longitude = float(query.get('longitude', [None])[0]) if query.get('longitude') else None

        hourly_params = []
        if 'hourly' in query:
            hourly_value = query['hourly'][0]
            hourly_params = hourly_value.split(',') if hourly_value else []

        timezone = query.get('timezone', [None])[0]
        if timezone:
            timezone = requests.utils.unquote(timezone)

        logger.info(f"Извлечено из URL: lat={latitude}, lon={longitude}, tz={timezone}")
        logger.info(f"Параметры hourly: {hourly_params}")

        return latitude, longitude, hourly_params, timezone

    except Exception as e:
        logger.error(f"Ошибка при парсинге URL: {e}")
        return None, None, [], None


def get_historical_weather(
        latitude: float,
        longitude: float,
        start_date: str,
        end_date: str,
        hourly_params: Optional[List[str]] = None,
        timezone: str = "Europe/Moscow"
) -> Optional[pd.DataFrame]:
    url = "https://archive-api.open-meteo.com/v1/archive"

    params_from_url = [
        "temperature_2m", "wind_speed_10m", "wind_speed_80m", "wind_speed_120m",
        "wind_speed_180m", "wind_direction_10m", "wind_direction_80m",
        "wind_direction_180m", "wind_gusts_10m", "wind_direction_120m",
        "precipitation", "relative_humidity_2m", "pressure_msl", "weather_code", "snowfall",
        "snow_depth", "cloud_cover", "cloud_cover_low", "cloud_cover_mid",
        "cloud_cover_high", "rain", "showers", "vapour_pressure_deficit",
        "apparent_temperature", "dew_point_2m", "et0_fao_evapotranspiration"
    ]

    final_params = hourly_params if hourly_params else params_from_url

    params = {
        "latitude": latitude,
        "longitude": longitude,
        "start_date": start_date,
        "end_date": end_date,
        "hourly": ",".join(final_params),
        "timezone": timezone
    }

    try:
        logger.info(f"Запрос к API: {url}")
        logger.info(f"Параметры: {params}")

        response = retry_session.get(url, params=params, timeout=60)
        response.raise_for_status()

        data = response.json()

        if data.get("error"):
            logger.error(f"API вернул ошибку: {data['reason']}")
            return None

        if "hourly" not in data or not data["hourly"]:
            logger.warning("Нет данных в ключе 'hourly'")
            return None

        df = pd.DataFrame(data["hourly"])

        df["time"] = pd.to_datetime(df["time"])
        df.set_index("time", inplace=True)

        for col in df.columns:
            df[col] = pd.to_numeric(df[col], errors='coerce')

        logger.info(f"Успешно загружено: {len(df)} записей, {len(df.columns)} переменных")
        logger.info(f"Столбцы: {list(df.columns)}")

        return df

    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP ошибка: {e}")
        if hasattr(e, 'response') and e.response is not None:
            logger.error(f"Response content: {e.response.text}")
        return None
    except requests.exceptions.Timeout:
        logger.error("Таймаут запроса к API")
        return None
    except requests.exceptions.RequestException as e:
        logger.error(f"Ошибка соединения: {e}")
        return None
    except Exception as e:
        logger.error(f"Неизвестная ошибка: {e}")
        return None


def create_storm_labels(
        df: pd.DataFrame,
        wind_threshold: float = 15.0,
        gust_threshold: float = 25.0,
        precip_threshold: float = 7.0,
        pressure_drop_window: int = 3,
        pressure_drop_threshold: float = 4.0,
        include_weather_code: bool = True
) -> pd.DataFrame:
    if df is None or df.empty:
        return df

    df = df.copy()
    storm_conditions = pd.Series(False, index=df.index)

    # 1. Сильный ветер на разных высотах
    wind_columns = [col for col in df.columns if col.startswith('wind_speed_')]
    for wind_col in wind_columns:
        storm_conditions |= (df[wind_col] >= wind_threshold)

    # 2. Порывы ветра
    if "wind_gusts_10m" in df.columns:
        storm_conditions |= (df["wind_gusts_10m"] >= gust_threshold)

    # 3. Сильные осадки
    precip_columns = ["precipitation", "rain", "showers"]
    for precip_col in precip_columns:
        if precip_col in df.columns:
            storm_conditions |= (df[precip_col] >= precip_threshold)

    # 4. Быстрое падение давления (штормовой признак)
    pressure_col = None
    for col in ["pressure_msl", "surface_pressure"]:
        if col in df.columns:
            pressure_col = col
            break

    if pressure_col:
        delta_p = df[pressure_col].diff(periods=pressure_drop_window)
        rapid_drop = delta_p < -pressure_drop_threshold
        storm_conditions |= rapid_drop.fillna(False)

    # 5. Опасные погодные коды
    if include_weather_code and "weather_code" in df.columns:
        storm_codes = [65, 75, 82, 85, 86, 95, 96, 99]
        storm_conditions |= df["weather_code"].isin(storm_codes)

    # 6. Высокая облачность (признак неустойчивости)
    cloud_columns = [col for col in df.columns if col.startswith('cloud_cover')]
    for cloud_col in cloud_columns:
        if cloud_col in df.columns:
            storm_conditions |= (df[cloud_col] >= 80)  # Облачность > 80%

    df["is_storm"] = storm_conditions.astype(int)
    storm_count = df["is_storm"].sum()
    logger.info(f"Создано меток шторма: {storm_count} из {len(df)} ({storm_count / len(df) * 100:.2f}%)")

    return df


def save_results(df: pd.DataFrame, filename: str, metadata: Optional[Dict] = None):
    try:
        os.makedirs('data', exist_ok=True)
        filepath = f"data/{filename}"

        df.to_csv(filepath, encoding='utf-8')
        logger.info(f"Данные сохранены: {filepath}")

        if metadata:
            metapath = filepath.replace('.csv', '_metadata.json')
            with open(metapath, 'w', encoding='utf-8') as f:
                json.dump(metadata, f, indent=2, ensure_ascii=False)
            logger.info(f"Метаданные сохранены: {metapath}")

    except Exception as e:
        logger.error(f"Ошибка при сохранении: {e}")


def main():
    source_url = (
        "https://open-meteo.com/en/docs?hourly=temperature_2m,wind_speed_10m,wind_speed_80m,"
        "wind_speed_120m,wind_speed_180m,wind_direction_10m,wind_direction_80m,wind_direction_180m,"
        "wind_gusts_10m,wind_direction_120m,precipitation,relative_humidity_2m,pressure_msl,weather_code,"
        "snowfall,snow_depth,cloud_cover,cloud_cover_low,cloud_cover_mid,cloud_cover_high,rain,"
        "showers,vapour_pressure_deficit,apparent_temperature,dew_point_2m,et0_fao_evapotranspiration&timezone=Europe%2FMoscow&"
        "latitude=55.7522&longitude=37.6156"
    )

    latitude, longitude, hourly_params, timezone = parse_parameters_from_url(source_url)

    if latitude is None or longitude is None:
        latitude, longitude = 55.7522, 37.6156
        logger.warning("Используются координаты по умолчанию: Москва")

    if not timezone:
        timezone = "Europe/Moscow"
        logger.warning("Используется временная зона по умолчанию: Europe/Moscow")

    start_date = '2022-01-01'
    end_date = '2025-09-18'

    logger.info("Запуск парсера погодных данных Open-Meteo")
    logger.info(f"Координаты: {latitude}, {longitude} | Таймзона: {timezone}")
    logger.info(f"Период: {start_date} — {end_date}")
    logger.info(f"Запрашиваемые параметры: {hourly_params}")

    df = get_historical_weather(
        latitude=latitude,
        longitude=longitude,
        start_date=start_date,
        end_date=end_date,
        hourly_params=hourly_params,
        timezone=timezone
    )

    if df is None or df.empty:
        logger.error("Не удалось получить данные или данные пустые.")
        return

    labeled_df = create_storm_labels(
        df,
        wind_threshold=15,
        gust_threshold=25,
        precip_threshold=7,
        pressure_drop_window=3,
        pressure_drop_threshold=4.0,
        include_weather_code=True
    )

    save_results(
        labeled_df,
        "storm_data.csv",
        metadata={
            "source_url": source_url,
            "location": {"lat": latitude, "lon": longitude},
            "timezone": timezone,
            "date_range": {"start": start_date, "end": end_date},
            "hourly_params": hourly_params,
            "storm_criteria": {
                "wind_speed_* >= km/h": 15,
                "wind_gusts_10m >= km/h": 25,
                "precipitation/rain/showers >= mm/h": 7,
                "pressure_drop >= hPa/3h": 4.0,
                "storm_weather_codes": [65, 75, 82, 85, 86, 95, 96, 99],
                "cloud_cover >= %": 80
            },
            "generated_at": datetime.now().isoformat(),
            "total_rows": len(labeled_df),
            "storm_events_count": int(labeled_df["is_storm"].sum()),
            "columns_list": list(labeled_df.columns)
        }
    )

    logger.info(f"Общее количество записей: {len(labeled_df)}")
    logger.info(f"Количество штормовых событий: {labeled_df['is_storm'].sum()}")
    logger.info(f"Доля штормовых событий: {labeled_df['is_storm'].mean() * 100:.2f}%")
    logger.info(f"Период данных: от {labeled_df.index.min()} до {labeled_df.index.max()}")

    logger.info("Готово: данные успешно получены и сохранены")


if __name__ == "__main__":
    main()
