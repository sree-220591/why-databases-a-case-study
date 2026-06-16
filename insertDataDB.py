import sqlite3

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

accounts = [
    (1001, "Alice", 10000),
    (1002, "Bob", 5000),
    (1003, "Charlie", 7000)
]

cursor.executemany("""
INSERT INTO accounts
VALUES (?, ?, ?)
""", accounts)

conn.commit()
conn.close()

print("Sample Accounts Added")