from flask import Flask
import pandas as pd
import requests
import datetime
from bs4 import BeautifulSoup
import googlescraper

app = Flask(__name__)

@app.route("/")
def search_page():
    html = '<div class="container-out">\n<div class="container-in">\n<div class="search-container">\n<div class="search-engine">\n<p class="search-title">Search Names\n</p>\n<input \ntype="input"\n id="search-input"\n autocomplete="off"\nplaceholder="Hit Enter to Search"\n/>\n</div>\n<div id="search-results"></div>\n<div id="search-data"></div>\n</div>\n</div>\n</div>'
    return html

if __name=="__main":
    app.run(host='0.0.0.0', port=5000)

    
