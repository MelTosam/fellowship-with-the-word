import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

print('--- FAVOURITES ---')
cursor.execute('SELECT * FROM favourites')
for row in cursor.fetchall():
    print(row)

print('--- USERS ---')
cursor.execute('SELECT id, name, email FROM users')
for row in cursor.fetchall():
    print(row)

print('--- DEVOTIONALS (first 5) ---')
cursor.execute('SELECT id, title FROM devotionals LIMIT 5')
for row in cursor.fetchall():
    print(row)

conn.close()
