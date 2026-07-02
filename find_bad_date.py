import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()
cursor.execute("SELECT id, title, date FROM devotionals WHERE date = 'o4-08-2026'")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
