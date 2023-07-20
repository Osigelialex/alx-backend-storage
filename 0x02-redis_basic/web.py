#!/usr/bin/python3
"""
A module that Implements an expiring web cache and tracker
"""
import requests
import redis
from typing import Union


def get_page(url: str) -> Union[str, None]:
    """obtains html content from url"""
    r = redis.Redis()

    response = requests.get(url)
    key = "count:" + url

    if not r.get(key):
        r.setex(key, 10,  0)
    else:
        r.incr(key)

    if response.status_code == 200:
        return response.text

    return None
