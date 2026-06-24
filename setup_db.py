import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS devotionals (
        id SERIAL PRIMARY KEY,
        title TEXT,
        verse TEXT,
        explanation TEXT,
        date TEXT
    )
''')

connection.commit()
cursor.close()
connection.close()

print('Database and table created successfully')
