from datetime import datetime, timezone
from dotenv import load_dotenv
import json
from config import get_mongo_connect

#NOTE: Single connection to MongoClient that stays open.
_coll=get_mongo_connect()

load_dotenv()

#1.Filter - this function will test data
def _jsonable(obj):
    """Make params safely storable (e.g., convert sets, etc.)."""
    try:
        json.dumps(obj)
        return obj
    except TypeError:
        return json.loads(json.dumps(obj, default=str))


#2.Log function.

def log_search(search_type: str, params: dict, results_count: int) -> None:
    """
    Write a log document about a search the user performed.
    - search_type: "keyword" | "genre_years"
    - params: e.g. {"keyword": "ace"} or {"genre":"Action","year_from":2000,"year_to":2006}
    - results_count: how many items were returned on the first page
    """
    doc = {
        "timestamp": datetime.now(timezone.utc).isoformat(),
        "search_type": str(search_type),
        "params": _jsonable(dict(params or {})),
        "results_count": int(results_count),
    }
    _coll.insert_one(doc)

# Optional: quick self-test
if __name__ == "__main__":
    print("Writing test log...")
    log_search("keyword", {"keyword": "as"}, 7)
    # Show the last inserted doc (most recent)
    last = _coll.find().sort([("_id", -1)]).limit(1)
    for d in last:
        print("Last log:", {k: d[k] for k in ("timestamp","search_type","params","results_count")})















