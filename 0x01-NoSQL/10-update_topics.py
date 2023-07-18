#!/usr/bin/env python3
"""
A module that changes all topics of a school document based on the name
"""


def update_topics(mongo_collection, name, topics):
  """updates topics based on name

  Args:
      mongo_collection (object): mongo collection object
      name (string): school name to update 
      topics (list): list of topics approached in the school
  """
  mongo_collection.update_many(
    {name: name},
    {"$set": {topics: topics}}
  )
