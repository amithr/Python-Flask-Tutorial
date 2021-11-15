import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

conn.execute('DROP TABLE students')

conn.execute('CREATE TABLE students (name TEXT, email_address TEXT, birthday TEXT, favorite_subject TEXT)')
print("Table created successfully")
conn.close()