import re


def join_url(url, *paths):
    """
    Joins individual URL strings together, and returns a single string.
    Usage::
        >>> util.join_url("example.com", "index.html")
        'example.com/index.html'
    """
    for path in paths:
        url = re.sub(r'/?$', re.sub(r'^/?', '/', path), url)
    return url
