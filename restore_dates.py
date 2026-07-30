import psycopg2
from dotenv import load_dotenv

load_dotenv()

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

restore_dates = [
    (9,  '01-08-2026'),
    (13, '02-08-2026'),
    (14, '03-08-2026'),
    (15, '04-08-2026'),
    (16, '05-08-2026'),
    (17, '06-08-2026'),
    (18, '07-08-2026'),
    (19, '08-08-2026'),
    (20, '09-08-2026'),
    (21, '10-08-2026'),
    (22, '11-08-2026'),
    (23, '12-08-2026'),
    (24, '13-08-2026'),
    (26, '14-08-2026'),
    (27, '15-08-2026'),
    (28, '16-08-2026'),
    (30, '17-08-2026'),
    (31, '18-08-2026'),
]

for devotional_id, date in restore_dates:
    cursor.execute('UPDATE devotionals SET date = %s WHERE id = %s', (date, devotional_id))
    print(f'Restored ID {devotional_id} -> {date}')

conn.commit()
cursor.close()
conn.close()
print('All dates restored to August')
