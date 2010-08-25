"""
pyforrst
========

A thin interface to Forrst API
"""

from urllib import FancyURLopener

try:
    import json
except ImportError:
    try:
        import simplejson as json
    except ImportError:
        raise Exception("A JSON parser is required, e.g., simplejson at " \
                        "http://pypi.python.org/pypi/simplejson/")

version_info = (0, 1)
__version__ = ".".join(map(str, version_info))
_BASE_URI = "http://api.forrst.com/api/v1/"


class ForrstError(Exception):
    pass


class ForrstAPIURLOpener(FancyURLopener):
    version = 'pyforrst/%s' % (__version__,)


urlopen = ForrstAPIURLOpener().open


def call(url):
    """
    Makes a call to Forrst API and handles failed status if so
    """
    u = urlopen(_BASE_URI + url)
    data = json.loads(u.read())['resp']
    if data['stat'] == 'fail':
        raise ForrstError("Request failed, reason: %s" % (data['reason'],))
    return data


def user_info(username):
    """
    Requests user's information by username
    """
    response = call("users/info?username=%s" % (username,))
    return response['user']


def user_info_by_id(id):
    """
    Requests user's information by id
    """
    response = call("users/info?id=%d" % (id,))
    return response['user']


def user_posts(username, since=None):
    """
    Requests user's posts
    """
    url = "users/posts?username=%s" % (username,)
    if since is not None:
        url = url + "&since=%d" % (since,)
    response = call(url)
    return response['posts']
