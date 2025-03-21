import math

# Константы для Земли
R_EARTH = 6300 * 1000  # Радиус Земли в метрах
G_EARTH = 10  # Ускорение свободного падения на Земле (м/с²)
T_EARTH = 24 * 3600  # Период обращения геостационарного спутника (24 часа в секундах)

# Константы для Марса
R_MARS = 3396 * 1000  # Радиус Марса в метрах
G_MARS = 3.711  # Ускорение свободного падения на Марсе (м/с²)

# Константы для Венеры
R_VENUS = 6052 * 1000  # Радиус Венеры в метрах
G_VENUS = 8.87  # Ускорение свободного падения на Венере (м/с²)


def calculate_geostationary_orbit_height(R, g, T):
    """
    Функция для расчета высоты геостационарного спутника.
    Входные параметры: радиус планеты (R), ускорение свободного падения (g), период обращения (T).
    Возвращает высоту геостационарного спутника.
    """
    r = (T * R * math.sqrt(g) / (2 * math.pi)) ** (2 / 3)
    return r - R  # Высота над поверхностью


def calculate_number_of_satellites(R, r):
    """
    Функция для расчета количества спутников для покрытия поверхности.
    Входные параметры: радиус планеты (R), расстояние до спутника (r).
    Возвращает количество спутников.
    """
    h = R - (R ** 2 / r)
    S_segment = 2 * math.pi * R * h
    S_total = 4 * math.pi * R ** 2
    return math.ceil(S_total / S_segment)


# Расчет для Земли
height_earth = calculate_geostationary_orbit_height(R_EARTH, G_EARTH, T_EARTH)
num_satellites_earth = calculate_number_of_satellites(R_EARTH, R_EARTH + height_earth)

print("Высота геостационарного спутника Земли:", math.floor(height_earth / 1000), "км")
print("Количество спутников для покрытия Земли:", num_satellites_earth)

# Расчет для Марса
T_MARS = 24 * 3600 + 37 * 60 + 22  # Период обращения для Марса (24 часа в секундах)
height_mars = calculate_geostationary_orbit_height(R_MARS, G_MARS, T_MARS)
print("Высота геостационарного спутника Марса:", math.floor(height_mars / 1000), "км")

# Расчет для Венеры
T_VENUS = 243 * 24 * 3600  # Период обращения для Венеры (243 земных дня)
height_venus = calculate_geostationary_orbit_height(R_VENUS, G_VENUS, T_VENUS)
print("Высота геостационарного спутника Венеры:", math.floor(height_venus / 1000), "км")
