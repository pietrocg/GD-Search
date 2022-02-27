import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup

url = "https://www.google.com/search?q="

search_term_raw = input("What to search: ") # used for file name too
target_site = input("Do you want to search on a specific site? (y/n) ")
if target_site == "y":
    target_site = input("Specify the site domain (example: twitter.com): ")
    target_site_formatted = "site%3A"+target_site+"+"
file_search = input("Do you want to search for a specific file type? (y/n)")
if file_search == "y":
    file_target = input("Specify file type: (example: pdf): ")
    file_target_formatted= "filetype%3A"+file_target+"+"
search_term_formatted = search_term_raw.replace(" ", "+")
if target_site == "y" and file_search == "n":
    search_term = url+target_site_formatted+search_term_formatted
if target_site == "n" and file_search == "y":
    search_term = url+file_target_formatted+search_term_formatted
if target_site == "y" and file_search == "y":
    search_term = url+target_site_formatted+file_target_formatted+search_term_formatted
else:
    search_term = url+search_term_formatted

user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.102 Safari/537.36 Edge/18.19582'
headers = {"user-agent" : user_agent}

response = requests.get(search_term, headers=headers)

# parses content from webpage
if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

results = []
try:
    for element in soup.find_all("div", class_="g"):
        anchors = element.find_all("a")
        if anchors:
            link = anchors[0]['href']
            if link != None:
                link = link.replace("https://", "")
                title = element.find('h3').text
                result = {"title": title, "link": link}
                results.append(result)
except(AttributeError, KeyError) as er:
    print("Attribute or Key error")
    pass

dataframe = pd.DataFrame(data=results)

print(dataframe)
date = datetime.datetime.now()

dataframe.to_csv(search_term_raw+"_scraping_results_"+str(date.strftime("%m"))+"_"+str(date.strftime("%d"))+"_"+str(date.strftime("%H"))+"_"+str(date.strftime("%M")))