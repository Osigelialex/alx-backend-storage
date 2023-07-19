#!/usr/bin/env python3
"""
A module that writes string to redis
"""
import redis
import uuid


class Cache:
    """
    defines a cache class

    functions:
        store(data) - stores data in redis
    """
    def __init__(self):
        """initializes the Cache"""
        _redis = redis.Redis().flushdb()

    def store(data) -> str:
        """
        stores data in redis using random key

        Args:
            data(string) - value to store in redis
        """
        random_key = uuid.uuid1()
        self._redis.set(random_key, data)
