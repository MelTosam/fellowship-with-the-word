import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

connection = psycopg2.connect(os.environ.get('DATABASE_URL'))
cursor = connection.cursor()

with open('sermons.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split('|')
            cursor.execute(
                'INSERT INTO sermons (title, date, description, video_url) VALUES (%s, %s, %s, %s)',
                (parts[0], parts[1], parts[2], parts[3])
            )

connection.commit()
cursor.close()
connection.close()

print('Sermons imported successfully')
