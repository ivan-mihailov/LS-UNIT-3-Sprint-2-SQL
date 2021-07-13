""" This is an example sql file """

# 1 Import SQLite 3
import sqlite3

# 2 Create a connection to database
conn = sqlite3.connect('rpg_db (1).sqlite3')

# 3. Create a cursor object
cur = conn.cursor()

# 4. Execute query
result = cur.execute("SELECT * FROM armory_item;")

# 5. Fetch results
print(result.fetchone())

# 6. Close connection to database
conn.close()