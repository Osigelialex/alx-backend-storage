#!/usr/bin/env python3
"""
A module that provides some stats about Nginx logs stored in MongoDB
"""


if __name__ == "__main__":
    from pymongo import MongoClient

    client = MongoClient()
    col = client.logs.nginx

    print("{} logs".format(col.count_documents))
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        docs = col.count_documents({'method': method})
        print("\tmethod {}: {}".format(method, docs))

    stats = col.count_documents({'method': 'GET', 'path': '/status'})
    print("{} status check".format(stats))
