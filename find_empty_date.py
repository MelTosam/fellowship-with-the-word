import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()
cursor.execute("SELECT id, title, date FROM devotionals WHERE date = '' OR date IS NULL")
rows = cursor.fetchall()
for row in rows:
    print(row)
connection.close()
