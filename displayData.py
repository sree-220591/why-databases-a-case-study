#Reading the data from accounts.csv file and displaying the account details based on user input.

import csv

account_number = input("Enter account number: ")

found = False

with open('accounts.csv',mode='r') as file:
    reader = csv.reader(file)
    for row in reader:
        if row[0] == account_number:
            print(f"Account Number: {row[0]}")
            print(f"Account Holder: {row[1]}")
            print(f"Balance: {row[2]}")
            found = True
            break
if not found:
    print("Account not found.")