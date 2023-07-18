#!/usr/bin/env python3
"""
A module to list all documents from collection
"""


def list_all(mongo_collection):
    """lists all documents in collection

    Args:
      mongo_collection (collection object):
        collection object to get documents from
    """
    return mongo_collection.find()
