import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM accounts")

accounts = cursor.fetchall()

for account in accounts:
    print(account)

conn.close()