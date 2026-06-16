#Creating an account 

import csv

with open('accounts.csv', mode='r') as file:
    file.readline()
    reader = csv.reader(file)
    
    last_account_number = 0
    for row in reader:
        last_account_number = int(row[0])

new_account_number = last_account_number + 1
account_holder = input("Enter account holder name: ")
initial_balance = input("Enter initial balance: ")

with open('accounts.csv', mode='a', newline='') as file:
    writer = csv.writer(file)
    writer.writerow([new_account_number, account_holder, initial_balance])  
print(f"Account created successfully! Account Number: {new_account_number}")
