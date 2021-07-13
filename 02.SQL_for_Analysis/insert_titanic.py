""" 
Copies titanic.csv file to PostgreSQL instance on ElephantSQL.
"""
import psycopg2

# Create connection to PostgreSQL instance on ElephantSQL
dbname = 'xuiaiwai'
user = 'xuiaiwai'
password = 'ZZ8HqWn89Gm50E4D-v-jOJZxVKUPUotA'
host = 'hattie.db.elephantsql.com'
p_conn = psycopg2.connect(dbname = dbname, user = user, \
    password = password, host = host)

# Set up PostgreSQL cursor object
p_cur = p_conn.cursor()

# Change user to SUPERUSER to allow COPY command to run
# CODE DOES NOT RUN BECAUSE SUPERUSER PRIVILEGES ARE NEEDED TO CHANGE ANOTHER 
# USER TO SUPERUSER
# p_cur.execute("ALTER USER xuiaiwai WITH SUPERUSER")

# Create Pclass, Sex as Enumerated Types
p_cur.execute("CREATE TYPE pclass AS ENUM ('1', '2', '3')")
p_cur.execute("CREATE TYPE sex AS ENUM ('male', 'female')")

# Create armory_weapon table on PostgreSQL instance on ElephantSQL
p_cur.execute("""
                CREATE TABLE IF NOT EXISTS titanic (
                    id SERIAL PRIMARY KEY,
                    Survived INTEGER,
                    Pclass pclass,
                    Name VARCHAR(200),
                    Sex sex,
                    Age INTEGER,
                    Siblings_Spouses_Aboard INTEGER,
                    Parents_Children_Aboard INTEGER,
                    Fare FLOAT)
                """)

# Copy data from titanic.csv into titanic table on PostgreSQL instance
# on ElephantSQL
p_cur.execute("COPY titanic FROM 'C:\\Users\\iamwe\\Desktop\\titanic.csv' DELIMITER ',' CSV HEADER")

# Verify data copy into titanic table on PostgreSQL instance on ElephantSQL
p_cur.execute("SELECT * FROM titanic")
p_cur.fetchall()

# Commit data to PostgreSQL instance on ElephantSQL
p_conn.commit()

# Close PostgreSQL cursor and connection objects
p_cur.close()
p_conn.close()