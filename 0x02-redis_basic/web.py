#!/usr/bin/python3
"""
A module that Implements an expiring web cache and tracker
"""
import requests
import redis
from typing import Union


def get_page(url: str) -> Union[bytes, None]:
    """obtains html content from url"""
    r = redis.Redis()
    response = requests.get(url).content
    key = "count:" + url

    if not r.get(key):
        r.set(key, 0)
        r.set('content', response)
        r.expire('content', 10)
    else:
        r.incr(key)

    if r.get('content'):
        return r.get('content')

    return response
