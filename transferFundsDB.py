import sqlite3

sender = int(input("Enter Sender Account Number : "))
receiver = int(input("Enter Receiver Account Number : "))
amount = float(input("Enter Amount : "))

conn = sqlite3.connect("bank.db")
cursor = conn.cursor()

try:

    # Find sender
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no = ?",
        (sender,)
    )

    sender_record = cursor.fetchone()

    if sender_record is None:
        print("Sender account does not exist.")
        conn.close()
        exit()

    # Find receiver
    cursor.execute(
        "SELECT balance FROM accounts WHERE account_no = ?",
        (receiver,)
    )

    receiver_record = cursor.fetchone()

    if receiver_record is None:
        print("Receiver account does not exist.")
        conn.close()
        exit()

    if sender == receiver:
        print("Sender and Receiver cannot be same.")
        conn.close()
        exit()

    sender_balance = sender_record[0]

    if sender_balance < amount:
        print("Insufficient Balance.")
        conn.close()
        exit()

    # Begin transaction

    cursor.execute("""
    UPDATE accounts
    SET balance = balance - ?
    WHERE account_no = ?
    """, (amount, sender))

    cursor.execute("""
    UPDATE accounts
    SET balance = balance + ?
    WHERE account_no = ?
    """, (amount, receiver))

    cursor.execute("""
    INSERT INTO ledger(from_account, to_account, amount)
    VALUES (?, ?, ?)
    """, (sender, receiver, amount))

    conn.commit()

    print("\nTransaction Successful")

except Exception as e:

    conn.rollback()
    print("Transaction Failed")
    print(e)

finally:
    conn.close()