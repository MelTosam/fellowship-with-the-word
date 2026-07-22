import psycopg2

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

cursor.execute("SELECT id, title FROM devotionals WHERE date LIKE '%-08-2026' ORDER BY id LIMIT 18")
rows = cursor.fetchall()

dates = [
    '13-07-2026', '14-07-2026', '15-07-2026', '16-07-2026',
    '17-07-2026', '18-07-2026', '19-07-2026', '20-07-2026',
    '21-07-2026', '22-07-2026', '23-07-2026', '24-07-2026',
    '25-07-2026', '26-07-2026', '27-07-2026', '28-07-2026',
    '29-07-2026', '30-07-2026'
]

for i, row in enumerate(rows):
    cursor.execute('UPDATE devotionals SET date = %s WHERE id = %s', (dates[i], row[0]))
    print(f'Updated: {row[1]} -> {dates[i]}')

conn.commit()
cursor.close()
conn.close()
print('Done - 18 devotionals updated for Apple review')
