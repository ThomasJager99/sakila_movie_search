import json
from functools import lru_cache



@lru_cache(maxsize=1)
def load_genres_map() -> dict[str, str]:
    """Download genre.json and caching the result.
    Key- genre name in lower register
    Value- original genre in normal register"""
    with open("genres.json", 'r', encoding='utf-8') as f:
        data = json.load(f)
    return {
        item['name'].strip().casefold(): item['name'].strip()
        for item in data
        if 'name' in item
    }











