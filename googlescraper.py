import feedparser
import json
from googleapiclient.discovery import build

def fetch_trending():

    trends_url = "https://trends.google.com/trends/trendingsearches/daily/rss?geo=US"

    results = []

    RSS = feedparser.parse(trends_url)

    RSS_titles = []

    for i in range(len(RSS.entries)):

        RSS_titles.append(RSS.entries[i]['title'])

    return RSS_titles

def fetch_top_google_results(terms):

    API_key = "AIzaSyAXYsw2-ZrU8jFKhdn4p5myf6aGqfwCseM"

    cx = 'c78ad6819d9115784'

    resource = build("customsearch", "v1", developerKey=API_key).cse()
    results = {}
    for term in terms:
        result = resource.list(q=term, cx=cx).execute()
        for item in result['items']:
            results[term] = item['link']
    print(results)
    return results



terms = fetch_trending()
results = fetch_top_google_results(terms)