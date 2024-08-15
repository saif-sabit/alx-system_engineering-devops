#!/usr/bin/python3
"""
"""
import requests


def top_ten(subreddit):
    """
    doc
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "user-Agent": "tajba/0.0.1 "
    }
    response = requests.get(url, headers=headers, allow_redirects=False)

    # Check if the subreddit is valid by looking at the status code
    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']
        for post in posts:
            print(post['data']['title'])
    else:
        print(None)
