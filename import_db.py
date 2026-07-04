import psycopg2
import json

NEON_URL = "postgresql://neondb_owner:npg_X4Ihzl2tAdpO@ep-raspy-king-atkm989g.c-9.us-east-1.aws.neon.tech/neondb?sslmode=require"

with open('backup.json', 'r') as f:
    data = json.load(f)

conn = psycopg2.connect(NEON_URL)
cursor = conn.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS devotionals (
        id SERIAL PRIMARY KEY,
        title TEXT,
        verse TEXT,
        explanation TEXT,
        date TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS sermons (
        id SERIAL PRIMARY KEY,
        title TEXT,
        date TEXT,
        description TEXT,
        video_url TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name TEXT,
        email TEXT UNIQUE,
        password_hash TEXT,
        created_at TEXT
    )
''')

cursor.execute('''
    CREATE TABLE IF NOT EXISTS favourites (
        id SERIAL PRIMARY KEY,
        user_id INTEGER,
        item_type TEXT,
        item_id INTEGER
    )
''')

# Import devotionals
for d in data['devotionals']:
    cursor.execute(
        'INSERT INTO devotionals (id, title, verse, explanation, date) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING',
        (d['id'], d['title'], d['verse'], d['explanation'], d['date'])
    )

# Import sermons
for s in data['sermons']:
    cursor.execute(
        'INSERT INTO sermons (id, title, date, description, video_url) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING',
        (s['id'], s['title'], s['date'], s['description'], s['video_url'])
    )

# Import users
for u in data['users']:
    cursor.execute(
        'INSERT INTO users (id, name, email, password_hash, created_at) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (id) DO NOTHING',
        (u['id'], u['name'], u['email'], u['password_hash'], u['created_at'])
    )

# Import favourites
for f in data['favourites']:
    cursor.execute(
        'INSERT INTO favourites (id, user_id, item_type, item_id) VALUES (%s, %s, %s, %s) ON CONFLICT (id) DO NOTHING',
        (f['id'], f['user_id'], f['item_type'], f['item_id'])
    )

# Reset sequences
cursor.execute("SELECT setval('devotionals_id_seq', (SELECT MAX(id) FROM devotionals))")
cursor.execute("SELECT setval('sermons_id_seq', (SELECT MAX(id) FROM sermons))")
cursor.execute("SELECT setval('users_id_seq', (SELECT MAX(id) FROM users))")
cursor.execute("SELECT setval('favourites_id_seq', (SELECT MAX(id) FROM favourites))")

conn.commit()
cursor.close()
conn.close()

print('Import complete')
print(f'Devotionals imported: {len(data["devotionals"])}')
print(f'Sermons imported: {len(data["sermons"])}')
print(f'Users imported: {len(data["users"])}')
print(f'Favourites imported: {len(data["favourites"])}')
