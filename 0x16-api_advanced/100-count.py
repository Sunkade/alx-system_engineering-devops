#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, hot_list=None):
    """
    Recursively queries the Reddit API, parses the title of all hot articles, and prints a sorted count of given keywords.

    :param subreddit: The subreddit to search.
    :param word_list: List of keywords.
    :param hot_list: List containing titles of hot articles. If not provided, it will be fetched.
    """
    if hot_list is None:
        hot_list = recurse(subreddit)

    if hot_list is None:
        return

    word_count = {}
    for word in word_list:
        word_count[word.lower()] = 0

    for title in hot_list:
        words = title.lower().split()
        for word in word_list:
            word_count[word.lower()] += words.count(word.lower())

    sorted_count = sorted(word_count.items(), key=lambda x: (-x[1], x[0]))

    for word, count in sorted_count
