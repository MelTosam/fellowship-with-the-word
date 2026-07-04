import psycopg2
import os
import json
from dotenv import load_dotenv

load_dotenv()

conn = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = conn.cursor()

# Export devotionals
cursor.execute('SELECT id, title, verse, explanation, date FROM devotionals')
devotionals = [{'id': r[0], 'title': r[1], 'verse': r[2], 'explanation': r[3], 'date': r[4]} for r in cursor.fetchall()]

# Export sermons
cursor.execute('SELECT id, title, date, description, video_url FROM sermons')
sermons = [{'id': r[0], 'title': r[1], 'date': r[2], 'description': r[3], 'video_url': r[4]} for r in cursor.fetchall()]

# Export users
cursor.execute('SELECT id, name, email, password_hash, created_at FROM users')
users = [{'id': r[0], 'name': r[1], 'email': r[2], 'password_hash': r[3], 'created_at': r[4]} for r in cursor.fetchall()]

# Export favourites
cursor.execute('SELECT id, user_id, item_type, item_id FROM favourites')
favourites = [{'id': r[0], 'user_id': r[1], 'item_type': r[2], 'item_id': r[3]} for r in cursor.fetchall()]

conn.close()

data = {
    'devotionals': devotionals,
    'sermons': sermons,
    'users': users,
    'favourites': favourites
}

with open('backup.json', 'w') as f:
    json.dump(data, f, indent=2)

print('Export complete')
print(f'Devotionals: {len(devotionals)}')
print(f'Sermons: {len(sermons)}')
print(f'Users: {len(users)}')
print(f'Favourites: {len(favourites)}')
