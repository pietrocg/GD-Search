# Imported modules

from flask import Flask, request, render_template, session, redirect
import googlescraper as scraper
import DBcalls as DB
import pypyodbc
from IPython.display import HTML
import configparser
from pathlib import Path

# opening DB connection

c = configparser.RawConfigParser()
c.read(Path.cwd() / 'config.ini')
config = dict(c.items('DETAILS'))
cursor, cnxn = DB.connect(config)
DB.tables(cursor, config)

app = Flask(__name__)

@app.route("/")

def results_page():

    results = DB.read(config)

    html = HTML(results.to_html(classes='table table-stripped'))

    return html

# Fetch google results and write them to the database

terms = scraper.fetch_trending()
results = scraper.fetch_google_results(terms)
DB.write(results, config)
page= results_page()


