import sqlite3

connection = sqlite3.connect('fellowship.db')
cursor = connection.cursor()

title = input('Enter title: ')
verse = input('Enter verse: ')
explanation = input('Enter explanation: ')
date = input('Enter date (DD-MM-YYYY): ')

cursor.execute(
    'INSERT INTO devotionals (title, verse, explanation, date) VALUES (?, ?, ?, ?)',
    (title, verse, explanation, date)
)

connection.commit()
connection.close()

print('Devotional added successfully')
