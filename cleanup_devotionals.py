import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()

cursor.execute('DELETE FROM devotionals WHERE id IN (1,2,3,4,5,6,7,8)')
cursor.execute('UPDATE devotionals SET date = %s WHERE id = 9', ('01-08-2026',))

connection.commit()
cursor.close()
connection.close()

print('Cleanup done')
