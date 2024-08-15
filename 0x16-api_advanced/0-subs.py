#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns
    the number of subscribers
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "user-Agent": "tajba/0.0.1"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()
        return results['data']['subscribers']
    else:
        return 0
