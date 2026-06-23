import sqlite3

connection = sqlite3.connect('fellowship.db')
cursor = connection.cursor()

with open('devotionals.txt', 'r') as file:
    for line in file:
        line = line.strip()
        if line:
            parts = line.split('|')
            cursor.execute(
                'INSERT INTO devotionals (title, verse, explanation, date) VALUES (?, ?, ?, ?)',
                (parts[0], parts[1], parts[2], parts[3])
            )

connection.commit()
connection.close()

print('Devotionals imported successfully')
