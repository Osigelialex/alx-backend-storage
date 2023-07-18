#!/usr/bin/env python3
"""
A module that provides some stats about Nginx logs stored in MongoDB
"""


def log_stats(mongo_collection):
    """logs stats about nginx collection

    Args:
        mongo_collection (collection): nginx collection
    """
    document_count = mongo_collection.count_documents({})
    print("{} logs".format(document_count))

    print("Methods")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]

    for method in methods:
        document_count = mongo_collection.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, document_count))

    checks = mongo_collection.count_documents({'method': 'GET',
                                              'path': '/status'})
    print("{} status check".format(checks))


if __name__ == '__main__':
    from pymongo import MongoClient

    client = MongoClient()
    db = client.logs
    collection = db.nginx
    log_stats(collection)
