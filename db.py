import sqlite3

conn = sqlite3.connect('DB/database.db')
print("Opened database successfully")

conn.execute('CREATE TABLE IF NOT EXISTS emotions (name text, create_date date, created_at timestamp)')
conn.execute('CREATE TABLE IF NOT EXISTS user (email_address text, created_at timestamp)')
print("Table created successfully")
conn.close()