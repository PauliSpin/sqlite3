import sqlite3
import time
import datetime
import random
import matplotlib.pyplot as plt
import matplotlib .dates as mdates
from matplotlib import style

style.use('fivethirtyeight')

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


def read_from_db():
    c.execute("SELECT keyword, unix FRoM stuffToPlot WHERE unix > 1591182126")
    for row in c.fetchall():
        print(row)  # Prints something like ('Python', 1591182126.5601425)


def graph_data():
    c.execute('SELECT unix, value FROM stuffToPlot')
    dates = []
    values = []
    for row in c.fetchall():
        # print(row[0])
        # print(datetime.datetime.fromtimestamp(row[0]))
        dates.append(datetime.datetime.fromtimestamp(row[0]))
        values.append(row[1])

    plt.plot_date(dates, values, '-')
    plt.show()


graph_data()

c.close()
conn.close()
