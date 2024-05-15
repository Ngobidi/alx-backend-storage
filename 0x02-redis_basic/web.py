#!/usr/bin/env python3
'''validate a module with tools for caching and tracking.
'''
import requests
import redis
import time
from functools import wraps
 
redis_conn = redis.StrictRedis(host='localhost', port=6379, db=0)
 
def cached_and_tracked(expires=10):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            url = args[0]
            cache_key = f"cache:{url}"
            count_key = f"count:{url}"
 
            '''validates if the output is cached.
            '''
            cached_result = redis_conn.get(cache_key)
            if cached_result:
                redis_conn.incr(count_key)
                return cached_result.decode('utf-8')
 
            '''Find the page and cache the output.
            '''
            response = func(*args, **kwargs)
            redis_conn.setex(cache_key, expires, response)
 
            '''Track the URL access_count.
            '''
            redis_conn.incr(count_key)
 
            return response
        return wrapper
    return decorator
 
def get_page(url):
    response = requests.get(url)
    return response.text
