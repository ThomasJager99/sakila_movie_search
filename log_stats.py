from dotenv import load_dotenv
from config import get_mongo_connect

#NOTE: One and only connection to MongoDB via MongoClient
_coll=get_mongo_connect()

#NOTE: Loading environment status
load_dotenv()

def top_5_by_frequency():
    """
    Return top-5 most frequent requests grouped by (search_type + params).
    Each result looks like:
      {"_id": {"search_type": "...", "params": {...}}, "count": <int>}
    """
    pipeline = [
        {"$group": {
            "_id": {"search_type": "$search_type", "params": "$params"},
            "count": {"$sum": 1}
        }},
        {"$sort": {"count": -1, "_id.search_type": 1}},
        {"$limit": 5}
    ]
    return list(_coll.aggregate(pipeline))

def last_5_unique():
    """
    Return last 5 unique requests (unique by search_type + params), keeping the most recent timestamp.
    Each result looks like:
      {"_id": {"search_type": "...", "params": {...}},
       "last_ts": <ISO string>, "results_count": <int>}
    """
    pipeline = [
        {"$sort": {"timestamp": -1, "_id": -1}},  # newest first
        {"$group": {
            "_id": {"search_type": "$search_type", "params": "$params"},
            "last_ts": {"$first": "$timestamp"},
            "results_count": {"$first": "$results_count"}
        }},
        {"$sort": {"last_ts": -1}},
        {"$limit": 5}
    ]
    return list(_coll.aggregate(pipeline))

# Optional self-test
# if __name__ == "__main__":
#     print("Top-5 by frequency:")
#     for i, d in enumerate(top_5_by_frequency(), 1):
#         print(f"{i}. {d['_id']} — {d['count']}")
#
#     print("\nLast 5 unique:")
#     for i, d in enumerate(last_5_unique(), 1):
#         print(f"{i}. {d['_id']} — last: {d['last_ts']} — results: {d['results_count']}")




