#!/usr/bin/env python3
"""
A module that writes string to redis
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any


class Cache:
    """
    cache class
    """
    def __init__(self) -> None:
        """initializes the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[int, float, str, bytes]) -> str:
        """
        stores data in redis using random key
        """
        key = uuid.uuid4()
        self._redis.set(str(key), (data))
        return str(key)

    def get(self, key: str, fn: Optional[Callable] = None) -> \
            Union[Any,  bytes, None]:
        """returns original type of key"""
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_int(self, key: bytes) -> int:
        """converts key to int type"""
        return int.from_bytes(key, "big")

    def get_str(self, key: bytes) -> str:
        """converts key to str type"""
        return str(key, 'UTF-8')
