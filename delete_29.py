import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()
cursor.execute("DELETE FROM devotionals WHERE id = 29")
connection.commit()
cursor.close()
connection.close()
print('Deleted')
