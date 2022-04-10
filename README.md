# GD-Search - Trendr
This project is designed to keep you up to date with the current trends on the internet.

# Usage

The purpose of this app is to provide a ‘one stop shop’ for the top 10 most trending topics on the internet weekly. The app presents the topics in a readable and accessible format. The links associated with each topic allow the user to read more about them.

To access the main webpage and check out the project, please click the following link:(INSERT_ip_address_HERE)

# Build
The main application was built using Flask, a python module which facilitates web development.

The database connected to the application was built using MySQL, a relational database management system. This database stores the information taken from the google search API, which is then displayed on the webpage.

The overall project runs on a Docker instance on the Google Cloud Platform (GCP).


# Imported modules
The following modules were used to ensure each aspect of the project ran as intended:
These are outlined in the requirements.txt file in the Github repository. The following is a more detailed version.
- mysql.connector
  - ClientFlag  
- pymysql as pdb
- flask
  - Flask, request, render_template, session, redirect
- googlescraper as scraper
- DBcalls as DB
- pypyodbc
- IPython.display
  - HTML
- configparser
- pathlib
  - Path
- feedparser
- json
- googleapiclient.discovery
  - build
- pandas as pd   

# Project information
This is a cloud computing project for the module ECS781P, taught by Dr.Sukhpal Singh Gill at Queen Mary University London.
