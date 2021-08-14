import praw
import re
import matplotlib.pylab as plt
import os
from dotenv import load_dotenv

load_dotenv()

""" 
Authentication
"""

reddit = praw.Reddit(client_id=os.getenv('CLIENT_ID'), 
                     client_secret=os.getenv('CLIENT_SECRET'), 
                     user_agent=os.getenv('USER_AGENT'))

""" 
Get hot posts from the WSB 🚀🚀🚀 subreddit 
"""
subreddit = reddit.subreddit('wallstreetbets')
hot_posts = subreddit.hot(limit=500)

""" 
Check each post for valid tickers and print the hottest mentioned stocks
"""
bigger_fish = []
for post in hot_posts:
    title_words = post.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$') and not re.search(r'\d', word), title_words)))
    if len(cashtags) > 0:
        bigger_fish.extend(cashtags)
        
print('\n*************************************')
data = {}        
for element in bigger_fish:
    data[element] = bigger_fish.count(element)
    # print(element, "\n", bigger_fish.count(element))

v=list(data.values())
k=list(data.keys())
print('Most mentioned ticker according to last 500 HOT posts in WSB: ', k[v.index(max(v))])
print('\n*************************************')

"""Show the top 10 mentioned tickers in a graph
"""
new = sorted(data, key=data.get, reverse=True)[:10]
newest = {}
for e in new:
    newest[e] = data.get(e)
plt.bar(*zip(*newest.items()))
plt.show()