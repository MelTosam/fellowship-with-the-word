import psycopg2

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS reading_history (
        id SERIAL PRIMARY KEY,
        user_id INTEGER NOT NULL,
        devotional_id INTEGER NOT NULL,
        read_date TEXT NOT NULL
    )
''')

conn.commit()
cursor.close()
conn.close()
print('Reading history table created')
