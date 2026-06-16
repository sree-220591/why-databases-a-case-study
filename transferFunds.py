# Transfer funds from one account to another

import csv

sender = input("Enter Sender Account Number : ")
receiver = input("Enter Receiver Account Number : ")
amount = float(input("Enter Amount : "))

accounts = []

with open("accounts.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        accounts.append(row)

sender_found = False
receiver_found = False

sender_index = -1
receiver_index = -1

for i, account in enumerate(accounts):

    if account["account_no"] == sender:
        sender_found = True
        sender_index = i

    if account["account_no"] == receiver:
        receiver_found = True
        receiver_index = i

if not sender_found:
    print("Sender account does not exist.")
    exit()

if not receiver_found:
    print("Receiver account does not exist.")
    exit()

if sender == receiver:
    print("Sender and Receiver cannot be the same.")
    exit()

sender_balance = float(accounts[sender_index]["balance"])

if sender_balance < amount:
    print("Insufficient Balance.")
    exit()

accounts[sender_index]["balance"] = str(
    sender_balance - amount
)

accounts[receiver_index]["balance"] = str(
    float(accounts[receiver_index]["balance"]) + amount
)

with open("accounts.csv", mode="w", newline="") as file:

    fieldnames = [
        "account_no",
        "name",
        "balance"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(accounts)

txn_id = 1

with open("ledger.csv", mode="r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        txn_id = int(row["txn_id"]) + 1

with open("ledger.csv", mode="a", newline="") as file:

    writer = csv.writer(file)

    writer.writerow([
        txn_id,
        sender,
        receiver,
        amount
    ])

print("\nTransaction Successful")
print(f"₹{amount} transferred from {sender} to {receiver}")