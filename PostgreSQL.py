import psycopg
from psycopg import rows

conn = psycopg.connect(
    host = 'localhost',
    port = '5432',
    database = 'appdb',
    user = 'app',
    password = 'p@ssw0rd')
cur = conn.cursor()
cur.execute('SELECT * FROM greeting')
row = cur.fetchall()
for row in rows:
    print(row[0])
conn.close()