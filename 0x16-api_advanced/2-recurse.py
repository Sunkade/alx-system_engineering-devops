#!/usr/bin/python3
'''
    This module contains the function recurse
'''
import requests
from sys import argv

def recurse(subreddit, hot_list=[], after=None):
    '''
        Recursively queries the Reddit API and returns a list
        containing the titles of all hot articles for a given subreddit.
    '''
    user = {'User-Agent': 'Lizzie'}
    params = {'limit': 100, 'after': after}
    url = requests.get(f'https://www.reddit.com/r/{subreddit}/hot/.json', headers=user, params=params)
    
    try:
        data = url.json().get('data')
        after = data.get('after')
        children = data.get('children')
        
        if after is not None and children:
            for post in children:
                hot_list.append(post.get('data').get('title'))
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    except Exception:
        return None

if __name__ == "__main__":
    result = recurse(argv[1])
    if result is not None:
        print(len(result))
    else:
        print("None")
