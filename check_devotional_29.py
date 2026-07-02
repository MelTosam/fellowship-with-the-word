import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()
cursor.execute("SELECT id, title, verse, explanation, date FROM devotionals WHERE id = 29")
row = cursor.fetchone()
print('ID:', row[0])
print('Title:', row[1])
print('Verse:', row[2])
print('Explanation:', row[3])
print('Date:', row[4])
connection.close()
