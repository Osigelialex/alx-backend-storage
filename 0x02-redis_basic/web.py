#!/usr/bin/python3
"""
A module that Implements an expiring web cache and tracker
"""
import requests
import redis
from typing import Union


def get_page(url: str) -> Union[str, None]:
    """obtains html content from url"""
    redis_client = redis.Redis()
    response = requests.get(url)
    key = "count:" + url

    if response.status_code == 200:
        redis_client.setex('content', 10, response.text)

    if not redis_client.get(key):
        redis_client.set(key, 10)
    else:
        redis_client.incr(key)

    if redis_client.get('content'):
        return redis_client.get('content')

    return response.text
