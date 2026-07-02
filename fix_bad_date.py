import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()
cursor.execute("UPDATE devotionals SET date = '04-08-2026' WHERE id = 15")
connection.commit()
cursor.close()
connection.close()
print('Fixed')
