import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup
import feedparser
import json
import requests

def fetch_trending():

    trends_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"

    results = []

    RSS = feedparser.parse(trends_url)

    RSS_titles = []

    for i in range(len(RSS.entries)):

        RSS_titles.append(RSS.entries[i]['title'])

    return RSS_titles

def fetch_top_google_results():

    url = "https://www.googleapis.com/customsearch/v1?"

    API_key = "AIzaSyAXYsw2-ZrU8jFKhdn4p5myf6aGqfwCseM"

    params = {'key': API_key, 'cx':'gd-search-1648827529904'}

    results = requests.request("GET", url, params=params)

    #result = json.loads(results.text)

    print(results.text)


print(fetch_trending())
print(fetch_top_google_results())