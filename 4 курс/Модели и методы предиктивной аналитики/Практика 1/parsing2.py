import requests
import time
import csv
from typing import List, Dict, Any

# Многомерный ряд
# https://pokeapi.co

BASE_URL = "https://pokeapi.co/api/v2"


def get_json(url: str) -> Dict[str, Any]:
    try:
        resp = requests.get(url, timeout=10)
        resp.raise_for_status()
        return resp.json()
    except requests.exceptions.RequestException as e:
        print(f"Ошибка при запросе {url}: {e}")
        return {}


def get_pokemon_list(limit: int = 100, offset: int = 0) -> List[Dict[str, Any]]:
    url = f"{BASE_URL}/pokemon?limit={limit}&offset={offset}"
    data = get_json(url)
    return data.get("results", [])


def get_encounter_locations(pokemon_url: str) -> str:
    location_url = pokemon_url + "/encounters"
    try:
        locations = get_json(location_url)
        if locations:
            names = {
                loc.get("location_area", {}).get("name", "unknown")
                for loc in locations if loc.get("location_area")
            }
            return ", ".join(sorted(names)[:10])
        return ""
    except:
        return ""


def get_evolution_chain(evolution_chain_url: str) -> str:
    if not evolution_chain_url:
        return ""

    data = get_json(evolution_chain_url)
    if not data:
        return ""

    def parse_chain(chain):
        name = chain.get("species", {}).get("name", "")
        evolves_to = chain.get("evolves_to", [])
        if not evolves_to:
            return name
        next_names = [parse_chain(evo) for evo in evolves_to]
        return " -> ".join([name] + next_names)

    return parse_chain(data.get("chain", {}))


def get_pokemon_details(pokemon_url: str) -> Dict[str, Any]:
    data = get_json(pokemon_url)
    if not data:
        return {}

    species_url = data.get("species", {}).get("url")
    species_data = get_json(species_url) if species_url else {}

    stats = {}
    for s in data.get("stats", []):
        stat_name = s["stat"]["name"]
        stats[stat_name] = s["base_stat"]

    types = [t["type"]["name"] for t in data.get("types", [])]
    type_1 = types[0] if len(types) > 0 else ""
    type_2 = types[1] if len(types) > 1 else ""

    # Способности
    abilities = []
    hidden_ability = ""
    for ab in data.get("abilities", []):
        if ab.get("is_hidden"):
            hidden_ability = ab["ability"]["name"]
        else:
            abilities.append(ab["ability"]["name"])
    ability_1 = abilities[0] if len(abilities) > 0 else ""
    ability_2 = abilities[1] if len(abilities) > 1 else ""

    moves = [m["move"]["name"] for m in data.get("moves", [])[:5]]
    while len(moves) < 5:
        moves.append("")

    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "base_experience": data.get("base_experience"),
        "height": data.get("height"),
        "weight": data.get("weight"),
        "order": data.get("order"),

        # Типы
        "type_1": type_1,
        "type_2": type_2,

        # Способности
        "ability_1": ability_1,
        "ability_2": ability_2,
        "hidden_ability": hidden_ability,

        "hp": stats.get("hp", 0),
        "attack": stats.get("attack", 0),
        "defense": stats.get("defense", 0),
        "special_attack": stats.get("special-attack", 0),
        "special_defense": stats.get("special-defense", 0),
        "speed": stats.get("speed", 0),

        # Движения (по столбцам)
        "move_1": moves[0],
        "move_2": moves[1],
        "move_3": moves[2],
        "move_4": moves[3],
        "move_5": moves[4],

        # Спрайты
        "sprite_default": data.get("sprites", {}).get("front_default"),
        "sprite_shiny": data.get("sprites", {}).get("front_shiny"),
        "sprite_artwork": data.get("sprites", {}).get("other", {}).get("official-artwork", {}).get("front_default"),

        # Species
        "color": species_data.get("color", {}).get("name"),
        "generation": species_data.get("generation", {}).get("name"),
        "habitat": species_data.get("habitat", {}).get("name") if species_data.get("habitat") else "",
        "shape": species_data.get("shape", {}).get("name"),

        "is_legendary": 1 if species_data.get("is_legendary", False) else 0,
        "is_mythical": 1 if species_data.get("is_mythical", False) else 0,
        "capture_rate": species_data.get("capture_rate"),
        "base_happiness": species_data.get("base_happiness"),
        "growth_rate": species_data.get("growth_rate", {}).get("name"),
        "egg_groups": ", ".join([eg["name"] for eg in species_data.get("egg_groups", [])]),

        # Эволюция
        "evolution_chain": get_evolution_chain(species_data.get("evolution_chain", {}).get("url")),

        # Локации
        "encounter_locations": get_encounter_locations(pokemon_url),
    }


def parse_all_pokemon(total_limit: int = 100, pause_sec: float = 0.1) -> List[Dict[str, Any]]:
    all_pokemon = []
    offset = 0
    batch_size = 100

    print(f"Начинаем сбор данных о {total_limit} покемонах...")

    while len(all_pokemon) < total_limit:
        remaining = total_limit - len(all_pokemon)
        current_batch = min(batch_size, remaining)

        batch = get_pokemon_list(limit=current_batch, offset=offset)
        if not batch:
            break

        for pokemon in batch:
            details = get_pokemon_details(pokemon["url"])
            if details:
                all_pokemon.append(details)
                print(f"{details['id']:>3} | {details['name']:<12} | {details['type_1']}/{details['type_2']}")

            time.sleep(pause_sec)

        offset += len(batch)

    print(f"Готово: {len(all_pokemon)} покемонов обработано.")
    return all_pokemon


def save_to_csv(data: List[Dict[str, Any]], filename: str = "pokemon_data.csv"):
    if not data:
        print("Нет данных для сохранения.")
        return

    fieldnames = [
        "id", "name", "base_experience", "height", "weight", "order",
        "type_1", "type_2",
        "hp", "attack", "defense", "special_attack", "special_defense", "speed",
        "ability_1", "ability_2", "hidden_ability",
        "move_1", "move_2", "move_3", "move_4", "move_5",
        "sprite_default", "sprite_shiny", "sprite_artwork",
        "color", "generation", "habitat", "shape",
        "is_legendary", "is_mythical", "capture_rate", "base_happiness",
        "growth_rate", "egg_groups", "evolution_chain", "encounter_locations"
    ]

    with open(filename, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

    print(f"Данные сохранены в '{filename}' ({len(data)} записей, {len(fieldnames)} столбцов)")


def main():
    pokemon_data = parse_all_pokemon(total_limit=100, pause_sec=0.1)
    save_to_csv(pokemon_data, "pokemon_data.csv")


if __name__ == "__main__":
    main()
