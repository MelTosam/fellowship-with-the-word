import sqlite3

connection = sqlite3.connect('fellowship.db')
cursor = connection.cursor()

cursor.execute('''
    CREATE TABLE devotionals (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        verse TEXT,
        explanation TEXT,
        date TEXT
    )
''')

connection.commit()
connection.close()

print('Database and table created successfully')
