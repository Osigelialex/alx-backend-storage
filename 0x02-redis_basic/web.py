#!/usr/bin/python3
"""
A module that Implements an expiring web cache and tracker
"""
import requests
import redis


def cache_response(method):
    """stores response from html page in redis cache"""
    def get_page(url):
        r = redis.Redis()
        response = method(url)
        key = "count:" + url

        if not r.get(key):
            r.set(key, 0)
            r.set('content', response)
            r.expire('content', 10)
        else:
            r.incr(key)
        return r.get('content')
    return get_page


@cache_response
def get_page(url: str):
    """obtains html content from url"""
    response = requests.get(url).content
    return response
