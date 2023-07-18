#!/usr/bin/env python3
"""
A module that returns the list of school having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
  """returns list of schools having a topic

  Args:
      mongo_collection (object): mongodb collection object
      topic (string): topic searched for
  """
  result = mongo_collection.find_all(
    {"topic": topic}
  )
  return result
