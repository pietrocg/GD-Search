# Imported modules

import mysql.connector
from mysql.connector.constants import ClientFlag
import pymysql as pdb


# establishes database connection

def connect(config):
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()  # connection cursor
    cursor.execute('CREATE DATABASE IF NOT EXISTS scraper')  # creates 'scraper' database, which is used for terms and articles
    cnxn.close()  # close database connection to reconnect later
    config['database'] = 'scraper'  # add new database to config dict
    cnxn = mysql.connector.connect(**config)
    cursor = cnxn.cursor()
    return cursor, cnxn

# Cursor encapsulates SQL query and carries out commands to create and populate tables.

def tables(cursor):
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

def write(input, cnxn):
    input.to_sql('scraper', cnxn)

# Reads results from the database and returns the results
    
def read(cnxn):
    query = 'SELECT * from articles;'
    results = pd.read_sql(query, cnxn)
    return results
