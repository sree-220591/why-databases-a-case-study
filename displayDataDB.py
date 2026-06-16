import sqlite3

account_no = int(input("Enter Account Number: "))

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

cursor.execute("""
SELECT *
FROM accounts
WHERE account_no = ?
""", (account_no,))

account = cursor.fetchone()

if account:
    print("\nAccount Found")
    print("Account Number :", account[0])
    print("Customer Name  :", account[1])
    print("Balance        :", account[2])
else:
    print("Account does not exist.")

conn.close()