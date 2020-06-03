import sqlite3

# https://www.youtube.com/watch?v=NCc5r7Wr7gg
# SentDex SQLite3 with Python 3

conn = sqlite3.connect('SENTDEX/tutorial.db')
c = conn.cursor()


def create_table():
    # Columns in the table are
    #   unix        REAL
    #   datestamp   TEXT
    #   keyword     TEXT
    #   value       REAL
    #
    # Capitals such as CREATE TABLE . . are the instructions to SQL; case-insensitive but easier to read
    c.execute(
        'CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute(
        "INSERT INTO stuffToPlot VALUES(1451255552, '2016-01-01', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()


create_table()
data_entry()
