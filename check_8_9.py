import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()
cursor.execute('SELECT id, title, explanation FROM devotionals WHERE id IN (8, 9)')
rows = cursor.fetchall()

for row in rows:
    print('ID:', row[0])
    print('Title:', row[1])
    print('Explanation:', row[2][:200])
    print('---')

connection.close()
