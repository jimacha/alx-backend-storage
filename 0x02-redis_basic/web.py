'''
first checks if the URL is in the cache
if it is, returns the cached HTML content
else,it makes an HTTP request to the URL
'''


import requests
from cachetools import TTLCache

'''Create a cache with a TTL of 10 seconds'''
cache = TTLCache(maxsize=100, ttl=10)

def get_page(url: str) -> str:
   '''Check if the URL is in the cache'''
    if url in cache:
     '''If cached, return the cached HTML content'''
        return cache[url]

    '''If not cached, make an HTTP request to the URL'''
    response = requests.get(url)
    html_content = response.text

    '''Store the HTML content in the cache with the URL as the key'''
    cache[url] = html_content

    '''Track the number of times the URL was accessed'''
    access_count_key = f"count:{url}"
    cache[access_count_key] = cache.get(access_count_key, 0) + 1

    '''Return the HTML content'''
    return html_content

''' Implement the caching functionality as a decorator'''
from functools import wraps

def cache_page(func):
    cache = TTLCache(maxsize=100, ttl=10)
    @wraps(func)
    def wrapper(url):
         '''Check if the URL is in the cache'''
        if url in cache:
            '''If cached, return the cached HTML content'''
            return cache[url]
        '''If not cached, call the original function and store the result in the cache'''
        html_content = func(url)
        cache[url] = html_content
        return html_content
    return wrapper

'''Usage of the decorator'''
@cache_page
def get_page_with_cache(url: str) -> str:
    response = requests.get(url)
    return response.text
