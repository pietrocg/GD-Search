import mysql.connector
from mysql.connector.constants import ClientFlag
import MySQLdb as pdb
import configparser

# cloud database config info, change when uploading to GCP
c = configparser.RawConfigParser()
c.read(open('.config'))
config = dict(c.items())
# establishes database connection

def db_connect(config):
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()  # connection cursor
    cursor.execute(
        'CREATE DATABASE IF NOT EXISTS scraper')  # creates 'scraper' database, which is used for terms and articles
    cnxn.close()  # close database connection to reconnect later

    config['database'] = 'scraper'  # add new database to config dict
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    return cursor


def db_tables(cursor):
    cursor.execute("CREATE TABLE IF NOT EXISTS terms ("
                   "term_ID INT NOT NULL,"
                   "term VARCHAR(45),"
                   "article_ID INT NOT NULL,"
                   "dateadded DATETIME"
                   "PRIMARY KEY ('term_ID')"
                   "UNIQUE INDEX 'TERM_ID_UNIQUE' ('term_ID' ASC) VISIBLE"
                   "UNIQUE INDEX 'ARTICLE_ID_UNIQUE' ('article_ID' ASC) VISIBLE"
                   "CONSTRAINT 'article_ID'"
                   "FOREIGN KEY ('article_ID')"
                   "REFERENCES 'scraper'.'articles' ('article_ID')"
                   "CONSTRAINT 'term_ID'"
                   "FOREIGN KEY ('term_ID')"
                   "REFERENCES 'scraper'.'articles' ('term_ID'))")

    cursor.execute("CREATE TABLE IF NOT EXISTS articles ("
                   "article_ID INT NOT NULL,"
                   "term_ID INT NOT NULL,"
                   "article_title VARCHAR(45),"
                   "article_URL VARCHAR(255),"
                   "dateadded DATETIME)"
                   "UNIQUE INDEX 'TERM_ID_UNIQUE' ('term_ID' ASC) VISIBLE"
                   "UNIQUE INDEX 'ARTICLE_ID_UNIQUE' ('article_ID' ASC) VISIBLE"
                   "CONSTRAINT 'article_ID'"
                   "FOREIGN KEY ('article_ID')"
                   "REFERENCES 'scraper'.'terms' ('article_ID')"
                   "CONSTRAINT 'term_ID'"
                   "FOREIGN KEY ('term_ID')"
                   "REFERENCES 'scraper'.'terms' ('term_ID'))")

    cnxn.commit()  # this commits changes to the database

def db_write(input, cursor):
    for line in input:
        cursor.execute("INSERT INTO articles ")




def db_read(cursor):
    pass
