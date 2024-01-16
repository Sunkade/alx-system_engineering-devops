#!/usr/bin/python3
'''
    This module contains the function top_ten
'''
import requests
from sys import argv

def top_ten(subreddit):
    '''
        Returns the top ten posts for a given subreddit
    '''
    user_agent = {'User-Agent': 'Lizzie'}
    url = f'https://www.reddit.com/r/{subreddit}/hot/.json?limit=10'
    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        try:
            for post in response.json().get('data', {}).get('children', []):
                print(post.get('data', {}).get('title'))
        except KeyError:
            print("Error: Unexpected JSON structure.")
    else:
        print(None)

if __name__ == "__main__":
    if len(argv) < 2:
        print("Please pass an argument for the subreddit to search.")
    else:
        top_ten(argv[1])
