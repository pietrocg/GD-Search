from flask import Flask

app = Flask(__name__)

@app.route("/")
def search_page():
    html = '<div class="container-out">\n<div class="container-in">\n<div class="search-container">\n<div class="search-engine">\n<p class="search-title">Search Names\n</p>\n<input \ntype="input"\n id="search-input"\n autocomplete="off"\nplaceholder="Hit Enter to Search"\n/>\n</div>\n<div id="search-results"></div>\n<div id="search-data"></div>\n</div>\n</div>\n</div>'
    return html

if __name__ == "__main__":
    app.run(ssl_context='adhoc')
    
