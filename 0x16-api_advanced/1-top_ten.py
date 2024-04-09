#!/usr/bin/python3
"""
"""


def top_ten(subreddit):
    """
    doc 
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "user-Agent": "Tajba/API "
    }
