import pandas as pd

df = pd.read_csv('buddymove_holidayiq.csv')
print(df.shape)
print(df.isna().sum().sum())

import sqlite3

conn = sqlite3.connect('buddymove_holidayiq.sqlite3')

#df.to_sql(name = 'review', con = conn)

cur = conn.cursor()
rows = "SELECT count(*) FROM review"
print(f'The number of rows in the new SQL database is:\
 {cur.execute(rows).fetchone()[0]}')

""" 
Calculate number of users who have reviewed at least 100 Nature and at least\
100 Shopping. 
"""
users_nat_shop = "SELECT count('User Id') FROM review \
    WHERE (Nature >= 100) AND (Shopping >= 100)"
print(f'Number of users who reviewed at least 100 Nature category and \
    also reviewed at least 100 in the Shopping category: \
{cur.execute(users_nat_shop).fetchone()[0]}')

""" Calculates average number of reviews in each category. """

avg_sports = "SELECT round(avg(Sports), 2) FROM review"
avg_religious = "SELECT round(avg(Religious), 2) FROM review"
avg_nature = "SELECT round(avg(Nature), 2) FROM review"
avg_theatre = "SELECT round(avg(Theatre), 2) FROM review"
avg_shop = "SELECT round(avg(Shopping), 2) FROM review"
avg_picnic = "SELECT round(avg(Picnic), 2) FROM review"
print(f'Average number of reviews in the Sports category is:\
 {cur.execute(avg_sports).fetchone()[0]}')
print(f'Average number of reviews in the Religious category is:\
 {cur.execute(avg_religious).fetchone()[0]}')
print(f'Average number of reviews in the Nature category is:\
 {cur.execute(avg_nature).fetchone()[0]}')
print(f'Average number of reviews in the Theatre category is:\
 {cur.execute(avg_theatre).fetchone()[0]}')
print(f'Average number of reviews in the Shopping category is:\
 {cur.execute(avg_shop).fetchone()[0]}')
print(f'Average number of reviews in the Picnic category is:\
 {cur.execute(avg_picnic).fetchone()[0]}')

conn.close()