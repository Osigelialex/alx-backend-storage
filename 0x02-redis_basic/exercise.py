#!/usr/bin/env python3
"""
A module that writes string to redis
"""
import redis
import uuid
from typing import Union, Callable, Optional, Any
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """count how many times methods of the Cache class are called"""
    key = method.__qualname__

    @wraps(method)
    def count(self, *args, **kwargs):
        """decorator"""
        self._redis.incr(key)
        return method(self, *args, **kwargs)
    return count 

def call_history(method: Callable) -> Callable:
    """stores the history of inputs and outputs for a function"""

    @wraps(method)
    def inner(self, *args, **kwargs):
        """inner method"""
        key1 = method.__qualname__ + ':inputs'
        key2 = method.__qualname__ + ':outputs'
        self._redis.rpush(key1, str(args))
        output = method(self, *args, **kwargs)
        self._redis.rpush(key2, str(output))
        return output
    return inner

class Cache:
    """
    cache class
    """
    def __init__(self) -> None:
        """initializes the Cache"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
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

    def replay(self, method: Callable) -> None:
        """replays history of function"""
        key = method.__qualname__
        count = self.get_int(self._redis.get(key))
        print(f"{key} was called {count} times")

