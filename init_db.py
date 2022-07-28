import sqlite3

connection = sqlite3.connect('database.db')

# with open('schema.sql') as f:
#     connection.executescript(f.read())

cur = connection.cursor()

title = "fadsf"

cur.execute(f'DELETE FROM todo WHERE title="{title}";')

connection.commit()
connection.close()