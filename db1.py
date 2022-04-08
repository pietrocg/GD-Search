import mysql.connector
from mysql.connector.constants import ClientFlag

# cloud database config info, change when uploading to GCP
config = {
    'user': 'root',
    'password': '1234',
    'host': '34.142.29.169',

}

# establishes database connection
cnxn = mysql.connector.connect(**config)

cursor = cnxn.cursor()  # connection cursor
cursor.execute(
    'CREATE DATABASE IF NOT EXISTS scraper')  # creates 'scraper' database, which is used for terms and articles
cnxn.close()  # close database connection to reconnect later

config['database'] = 'scraper'  # add new database to config dict
cnxn = mysql.connector.connect(**config)
cursor = cnxn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS terms ("
               "term_ID INT NOT NULL AUTO-INCREMENT,"
               "term VARCHAR(45),"
               "article_ID INT NOT NULL,"
               "dateadded DATETIME)"
               "CONSTRAINT terms_pk PRIMARY KEY (term_ID)");

cursor.execute("CREATE TABLE IF NOT EXISTS articles ("
               "article_ID INT NOT NULL AUTO-INCREMENT,"
               "term_ID INT NOT NULL,"
               "article_title VARCHAR(45),"
               "article_URL VARCHAR(255),"
               "dateadded DATETIME)"
               "CONSTRAINT articles_pk PRIMARY KEY (article_ID)"
               "CONSTRAINT articles_fk FOREIGN KEY(article_ID) REFERENCES terms(term_ID) [ON DELETE{CASCADE}] [ON UPDATE{CASCADE}])";

cnxn.commit()  # this commits changes to the database
