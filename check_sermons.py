import psycopg2

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()
cursor.execute('SELECT id, title, date FROM sermons')
rows = cursor.fetchall()
for row in rows:
    print(row)
conn.close()
