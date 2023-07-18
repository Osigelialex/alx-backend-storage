#!/usr/bin/env python3
"""
A module that provides some stats about Nginx logs stored in MongoDB
"""
from pymongo import MongoClient


if __name__ == "__main__":
    client = MongoClient()
    col = client.logs.nginx

    print(f"{col.count_documents()} logs")
    print("Methods:")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        print(f"\tmethod {method}: \
          {col.count_documents({'method': method})}")

    stats = col.count_documents({'method': 'GET', 'path': '/status'})
    print(f"{stats} status check")
