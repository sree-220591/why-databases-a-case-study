import sqlite3

# Connect to database
conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

# User input
name = input("Enter Customer Name : ")
balance = float(input("Enter Initial Deposit : "))

# Find highest account number
cursor.execute("""
SELECT MAX(account_no)
FROM accounts
""")

max_account = cursor.fetchone()[0]

# Generate next account number
if max_account is None:
    new_account_no = 1001
else:
    new_account_no = max_account + 1

# Insert new account
cursor.execute("""
INSERT INTO accounts(account_no, customer_name, balance)
VALUES (?, ?, ?)
""", (new_account_no, name, balance))

conn.commit()

print("\nAccount Created Successfully")
print("Account Number :", new_account_no)

conn.close()