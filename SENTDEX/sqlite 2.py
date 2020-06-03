import sqlite3
import time
import datetime
import random

conn = sqlite3.connect('SENTDEX/tutorial.db')
c = conn.cursor()


def create_table():
    c.execute(
        'CREATE TABLE IF NOT EXISTS stuffToPlot(unix REAL, datestamp TEXT, keyword TEXT, value REAL)')


def data_entry():
    c.execute(
        "INSERT INTO stuffToPlot VALUES(1451255552, '2016-01-01', 'Python', 8)")
    conn.commit()
    c.close()
    conn.close()


def dynamic_data_entry():
    unix = time.time()
    date = str(datetime.datetime.fromtimestamp(
        unix).strftime('%Y-%m-%d %H:%M:%S'))
    keyword = 'Python'
    value = random.randrange(0, 10)
    # Column titles
    c.execute("INSERT INTO stuffToPlot (unix, datestamp, keyword, value) VALUES (?, ?, ?, ?)",
              (unix, date, keyword, value))
    conn.commit()   # Don't close the connection as we are going to loop and insert 10 things


create_table()

for i in range(10):
    dynamic_data_entry()
    time.sleep(1)   # Make sure the time clicks up at least 1 second
    print('pip')

c.close()
conn.close()
