from flask import Flask
import googlescraper as scraper
import DBcalls as DB
import pypyodbc


app = Flask(__name__)

@app.route("/")

def search_page(results):

    html = '<table>'
    '<caption>Trending Topics on the Interwebs Today</caption>'
    '<tr>'
    '  <th>Trending Term</th>'
    '  <th>Links</th>'
    '</tr>'
    '<tr>'
    '  <td>%s</td>'%results
    '  <td>Freecode Camp</td>'
    '  <td>Enki</td>'
    '</tr>'
    '<tr>'
    '  <td>W3Schools</td>'
    '  <td>Academind</td>'
    '  <td>Programming Hero</td>'
    '</tr>'\
    '<tr>'
    '  <td>Khan Academy</td>'
    '  <td>The Coding Train</td>'
    '  <td>Solo learn</td>'
    '</tr>'
    '</table>'
    return html

    
terms = scraper.fetch_trending()
results = scraper.fetch_google_results(terms)
print(results)
sorted_results = [results[i] for i in results.keys]
print(sorted_results)