import sqlite3
import os

DB_path = 'CODEMY/customer.db'
# Connect to Database
conn = sqlite3.connect(DB_path)

# Create a Cursor
c = conn.cursor()


# c.execute("""
#         CREATE TABLE customers (
#             first_name text,
#             last_name text,
#             email text
#         )
#         """)

# SQLite3 only has five DATATYPES
#   NULL
#   INTEGER
#   REAL
#   TEXT
#   BLOB

# c.execute("INSERT INTO customers VALUES ('Alice', 'Brown', 'Alice@email.com')")
# c.execute("INSERT INTO customers VALUES ('Bob', 'Grey', 'Bob@email.com')")
# c.execute("INSERT INTO customers VALUES ('Charlie', 'Black', 'Charlie@email.com')")

many_customers = [
    ('Wes', 'White', 'wes@email.com'),
    ('Steph', 'Blue', 'steph@email.com'),
    ('Don', 'Purple', 'don@email.com')
]

c.execute("INSERT INTO customers VALUES(?, ?, ?)", many_customers)

# c.execute("SELECT * FROM customers")
# c.fetchone()
# c.fetchmany(3)
# print(c.fetchall())

# Commit command above
conn.commit()

# Close Connection
conn.close()
