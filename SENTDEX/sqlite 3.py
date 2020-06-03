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


def read_from_db():
    # c.execute('SELECT * FROM stuffToPlot')
    # -----------------------------------------------------------------------------------
    # Using a single fetch statement for all data
    # data = c.fetchall()
    # print(data)
    # -----------------------------------------------------------------------------------
    # Using a for loop to step through each row
    # for row in c.fetchall():
    # print(row)
    # -----------------------------------------------------------------------------------
    # Using a WHERE clause
    # c.execute("SELECT * FROM stuffToPlot WHERE value=3 AND keyword='Python'")
    # for row in c.fetchall():
    #     print(row)
    # -----------------------------------------------------------------------------------
    # Using a WHERE clause with AND
    # c.execute(
    #     "SELECT * FROM stuffToPlot WHERE unix > 1591182100 AND unix < 1591182126")
    # for row in c.fetchall():
    #     print(row)
    # print(row[0])
    # Prints out something like: (1591182123.4943686, '2020-06-03 12:02:03', 'Python', 8.0)
    # Can pick out each item in this using an index, row[0] will print 1591182123.4943686
    # -----------------------------------------------------------------------------------
    # Can also be selective in the columns that you wish to select - does not have to be
    # the same order as in the DB
    c.execute("SELECT keyword, unix FRoM stuffToPlot WHERE unix > 1591182126")
    for row in c.fetchall():
        print(row)  # Prints something like ('Python', 1591182126.5601425)

# create_table()
# # data_entry()
# for i in range(10):
#     dynamic_data_entry()
#     time.sleep(1)   # Make sure the time clicks up at least 1 second
#     print('pip')


read_from_db()

c.close()
conn.close()
