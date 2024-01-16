#!/usr/bin/python3
"""
100-count
"""
import requests

def count_words(subreddit, word_list, hot_list=None):
    """
    Prints a sorted count of given keywords in the titles of hot articles for a subreddit.

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

    for word, count in sorted_count:
        if count > 0:
            print(f"{word}: {count}")

def recurse(subreddit, hot_list=None, after=None):
    """
    Returns a list containing titles of all hot articles for a given subreddit.

    :param subreddit: The subreddit to search.
    :param hot_list: List containing titles of hot articles.
    :param after: Token to get the next set of results.
    :return: List of titles.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
    
    params = {'limit': 100, 'after': after} if after else {'limit': 100}

    response = requests.get(url, headers=headers, params=params, allow_redirects=False)

    if response.status_code == 200:
        data = response.json()
        children = data['data']['children']
        hot_list = [post['data']['title'] for post in children]

        after = data['data']['after']
        if after:
            return recurse(subreddit, hot_list, after)
        else:
            return hot_list
    else:
        return None

if __name__ == '__main__':
    import sys

    if len(sys.argv) < 3:
        print("Usage: {} <subreddit> <list of keywords>".format(sys.argv[0]))
        print("Ex: {} programming 'python java javascript'".format(sys.argv[0]))
    else:
        count_words(sys.argv[1], [x for x in sys.argv[2].split()])
