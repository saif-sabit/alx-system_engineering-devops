#!/usr/bin/python3

"""
Function that queries the Reddit API and returns the number of subscribers.
"""

import requests


def number_of_subscribers(subreddit):
    """
    A function that queries the Reddit API and returns
    the number of subscribers for a given subreddit.

    Args:
        subreddit (str): The name of the subreddit to query.

    Returns:
        int: The number of subscribers for the subreddit, or 0 if the subreddit
        is invalid or does not exist.
    """

    url = f'https://www.reddit.com/r/{subreddit}/about.json'
    headers = {
        "User-Agent": "tajba/0.0.1"
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    if response.status_code == 200:
        results = response.json()
        return results['data']['subscribers']
    else:
        return 0
