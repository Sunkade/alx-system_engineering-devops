#!/usr/bin/python3
"""
1-top_ten
"""
import requests
from sys import argv

def top_ten(subreddit):
    """
    Prints the titles of the first 10 hot posts listed for a given subreddit.
    """
    user_agent = {'User-Agent': 'Lizzie'}
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json().get('data', {}).get('children', [])
        for post in data:
            print(post['data']['title'])
    else:
        print(None)

if __name__ == '__main__':
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(argv[1])
