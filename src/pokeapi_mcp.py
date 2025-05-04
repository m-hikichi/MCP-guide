import posixpath
from pathlib import PurePosixPath
from urllib.parse import urljoin, urlparse

import requests
from rich import print
from mcp.server.fastmcp import FastMCP

# MCPサーバーインスタンスの作成
mcp = FastMCP("pokeapi", log_level="INFO")

POKEAPI_BASE = "https://pokeapi.co/api/v2/"

# 日本語での能力値名マッピング
STAT_NAMES_JP = {
    "hp": "HP",
    "attack": "攻撃",
    "defense": "防御",
    "special-attack": "特攻",
    "special-defense": "特防",
    "speed": "素早さ",
}


# 日本語でのタイプ名マッピング（全タイプを網羅）
TYPE_NAMES_JP = {
    "normal": "ノーマル",
    "fire": "ほのお",
    "water": "みず",
    "grass": "くさ",
    "electric": "でんき",
    "ice": "こおり",
    "fighting": "かくとう",
    "poison": "どく",
    "ground": "じめん",
    "flying": "ひこう",
    "psychic": "エスパー",
    "bug": "むし",
    "rock": "いわ",
    "ghost": "ゴースト",
    "dark": "あく",
    "dragon": "ドラゴン",
    "steel": "はがね",
    "fairy": "フェアリー",
}


@mcp.tool()
def get_pokemon_info(pokemon_id: int) -> dict:
    """
    ポケモン基本情報（タイプ、特性、体重、高さ、種族値）を取得
    """
    path_segments = ["pokemon", str(pokemon_id)]
    relative_path = posixpath.join(*path_segments)
    ability_url = urljoin(POKEAPI_BASE, relative_path)

    try:
        response = requests.get(ability_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        # ネットワークエラーやステータスコードエラー
        raise RuntimeError(f"ポケモン情報の取得に失敗しました: {e}")

    data = response.json()

    species = get_pokemon_species_info(pokemon_id)
    types = [TYPE_NAMES_JP.get(t["type"]["name"]) for t in data["types"]]

    height = data["height"] / 10  # m
    weight = data["weight"] / 10  # kg

    stats = {s["stat"]["name"]: s["base_stat"] for s in data["stats"]}

    abilities = [
        get_ability_info(PurePosixPath(urlparse(a["ability"]["url"]).path).name)
        for a in data["abilities"]
    ]

    return {
        "species": species,
        "types": types,
        "height": height,
        "weight": weight,
        "stats": stats,
        "abilities": abilities,
    }


@mcp.tool()
def get_pokemon_species_info(pokemon_id: int) -> dict:
    """
    日本語のポケモン名と種別情報、ポケモン図鑑説明文を取得
    """
    path_segments = ["pokemon-species", str(pokemon_id)]
    relative_path = posixpath.join(*path_segments)
    ability_url = urljoin(POKEAPI_BASE, relative_path)

    try:
        response = requests.get(ability_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        # ネットワークエラーやステータスコードエラー
        raise RuntimeError(f"特性情報の取得に失敗しました: {e}")

    data = response.json()

    name = None
    for entry in data["names"]:
        lang = entry["language"]["name"]
        if lang in ("ja", "ja-Hrkt"):
            name = entry["name"]
            break

    genus = None
    for entry in data["genera"]:
        lang = entry["language"]["name"]
        if lang in ("ja", "ja-Hrkt"):
            genus = entry["genus"]
            break

    flavor_text_entries = []
    for entry in data["flavor_text_entries"]:
        lang = entry["language"]["name"]
        if lang == "ja":
            flavor_text_entries.append({
                "version": entry["version"]["name"],
                "flavor_text": entry["flavor_text"],
            })
    
    return {
        "name": name,
        "genus": genus,
        "flavor_text_entries": flavor_text_entries,
    }



@mcp.tool()
def get_ability_info(ability_id: int) -> dict:
    """
    日本語の特性名と効果説明文を取得
    """
    path_segments = ["ability", str(ability_id)]
    relative_path = posixpath.join(*path_segments)
    ability_url = urljoin(POKEAPI_BASE, relative_path)

    try:
        response = requests.get(ability_url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        # ネットワークエラーやステータスコードエラー
        raise RuntimeError(f"特性情報の取得に失敗しました: {e}")

    data = response.json()

    name = None
    for entry in data["names"]:
        lang = entry["language"]["name"]
        if lang in ("ja", "ja-Hrkt"):
            name = entry["name"]
            break

    description = None
    for entry in data["flavor_text_entries"]:
        lang = entry["language"]["name"]
        if lang in ("ja", "ja-Hrkt"):
            description = entry["flavor_text"]
            break

    return {
        "name": name,
        "description": description,
    }


if __name__ == "__main__":
    # print(get_ability_info(1))
    # print(get_pokemon_species_info(1))
    # print(get_pokemon_info(1))
    mcp.run()
