#!/usr/bin/python3
'''
    This module contains the function count_words
'''
import requests
from sys import argv

def count_words(subreddit, word_list, hot_list=[], after=None):
    '''
        Recursively queries the Reddit API, parses the title of all hot articles,
        and prints a sorted count of given keywords.
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
            
            return count_words(subreddit, word_list, hot_list, after)
        else:
            print_word_count(word_list, hot_list)
    except Exception:
        print(None)

def print_word_count(word_list, hot_list):
    '''
        Prints the sorted count of given keywords.
    '''
    word_count = {}
    for word in word_list:
        word_count[word.lower()] = 0
    
    for title in hot_list:
        for word in word_list:
            word_count[word.lower()] += title.lower().split().count(word.lower())
    
    sorted_word_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))
    
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

if __name__ == "__main__":
    if len(argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(argv[0]))
        print("Ex: {} programming 'python java javascript'".format(argv[0]))
    else:
        count_words(argv[1], [x for x in argv[2].split()])
