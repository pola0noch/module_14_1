import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')
connection.commit()

for i in range(1, 11):
    cursor.execute('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', (f'User{i}', f'example{i}@gmail.com', str(10 * i), '1000'))
connection.commit()

cursor.execute('UPDATE Users SET balance = ? WHERE id % 2 != 0', (500,))
connection.commit()

cursor.execute('DELETE FROM Users WHERE id % 3 = 1')
connection.commit()

cursor.execute('SELECT username, email, age, balance  FROM Users WHERE age != ?', (60,))
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]}, Email: {user[1]}, Возраст: {user[2]}, Баланс: {user[3]}')
connection.commit()
connection.close()

