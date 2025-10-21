import json
from functools import lru_cache


#NOTE: This func contain inside cash from genre.json file and transform it into
# more useful dict{action:Action} in cash so we can launch validation faster O(1)
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

#NOTE: Tool is working and successfully refreshes the genre list from .json to dict
def reload_genres():
    """Clearing cash and creating new stuck from latest
    version of genres and years"""
    load_genres_map.caсhe_clear()

#NOTE: This one will show that func is working correctly and inside is dict
# print(load_genres_map())







