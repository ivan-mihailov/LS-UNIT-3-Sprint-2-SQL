""" 
Moves database from SQLite3 to PostgreSQL instance on ElephantSQL.
"""
import sqlite3
import psycopg2

# Set up SQLite3 connection object
s_conn = sqlite3.connect(r'C:\Users\iamwe\Documents\09.Coding\Lambda_School\Data_Science\03.Unit_3\02.SQL\rpg_db.sqlite3')
# Set up SQLite3 cursor object
s_cur = s_conn.cursor()

# Copy armory_weapons data from SQLite3 database
rows_aw = s_cur.execute("SELECT item_ptr_id, power FROM armory_weapon").fetchall()

# Create connection to PostgreSQL instance on ElephantSQL
dbname = 'xuiaiwai'
user = 'xuiaiwai'
password = 'ZZ8HqWn89Gm50E4D-v-jOJZxVKUPUotA'
host = 'hattie.db.elephantsql.com'
p_conn = psycopg2.connect(dbname = dbname, user = user, \
    password = password, host = host)

# Set up PostgreSQL cursor object
p_cur = p_conn.cursor()

# Create armory_weapon table on PostgreSQL instance on ElephantSQL
p_cur.execute("""
                CREATE TABLE IF NOT EXISTS armory_weapon (
                    item_ptr_id INTEGER,
                    power INTEGER)
                """)

# Insert data into armory_weapon table on PostgreSQL instance on ElephantSQL
values = ','.join(['%s'] * len(rows_aw))
insert_query = "INSERT INTO armory_weapon (item_ptr_id, power) values {}".format(values)
p_cur.execute(insert_query, rows_aw)

# Verify data insertion into armory_weapons table on PostgreSQL 
# instance on ElephantSQL
p_cur.execute("SELECT * FROM armory_weapon")
p_cur.fetchall()


# Commit data to PostgreSQL instance on ElephantSQL
p_conn.commit()

# Close PostgreSQL cursor and connection objects
p_cur.close()
p_conn.close()