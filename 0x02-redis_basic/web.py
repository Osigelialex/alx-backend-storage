#!/usr/bin/python3
"""
A module for implementing a web cache and tracker
"""
import redis
import requests
from requests.exceptions import InvalidURL, RequestException


def get_page(url: str) -> str:
    """
    Obtains html from a page and displays it
    """
    redis_client = redis.Redis()
    key = 'count:' + url
    CACHE_EXPIRY = 10

    # increment tracker count for url
    if not redis_client.exists(key):
        redis_client.set(key, 0)
    else:
        redis_client.incr(key)

    # check for cached content
    if redis_client.exists(url):
        cached_content = redis_client.get(url).decode('utf-8')
        return cached_content

    # cache response with expiry
    try:
        response = requests.get(url)
        html_content = response.text
        redis_client.setex(url, CACHE_EXPIRY, html_content.encode('utf-8'))
        return str(html_content)
    except InvalidURL as e:
        print('Invalid URL', e)
    except RequestException as e:
        print('Error', e)

    return ''
