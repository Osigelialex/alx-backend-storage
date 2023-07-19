#!/usr/bin/env python3
"""
A module that writes string to redis
"""
import redis
import uuid


class Cache:
    """
    cache class
    """
    def __init__(self):
        """initializes the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data) -> str:
        """
        stores data in redis using random key
        """
        key = uuid.uuid4()
        self._redis.set(str(key), (data))
        return str(key)

