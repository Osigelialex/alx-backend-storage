#!/usr/bin/env python3
""" 
A module that inserts a new document in a collection based on kwargs
"""


def insert_school(mongo_collection, **kwargs):
  """inserts a new document in a collection based on kwargs

  Args:
      mongo_collection (object): mongo collection object
  """
  mongo_collection.insert_one(kwargs)
  return mongo_collection.inserted_id
