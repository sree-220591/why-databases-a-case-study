Case Study : A Bank Transaction
<br>
**Banking Transaction System**<br>
Consider a simple banking system where a person can open a new account, transfer fund to an existing account and check the history of all her transactions till date.

The application performs the following checks:<br>
-If the account balance is not enough it will not allow the fund transfer.<br>
-If the account numbers are not correct, it will flash a message and terminate the transaction.<br>
-If a transaction is successful, it prints a confirmation message<br>

We will use this banking transaction system to compare various features of a file-based implementation vs a DBMS-based implementation.<br>

*File-based Implementation*<br>
-Account details stored in accounts.csv<br>
-Transaction details stored in ledger.csv
<br>


*Limitations of the File-based Implementation*<br>
1) A File system cannot guarantee **Atomicity**.<br>
2) **Searching** becomes difficult with the increasing data as it has to read the entire file to search for a single account.<br>
3) Cannot be consistent over time, since if two users simultaneously create accounts, both may get the same account number.<br>
4) It doesnot suit well for implementing **constraints.**<br>

<br>Now comes the heart of our System.<br>

*DBMS-based Implementation*<br>
In the DBMS-based implementation, the same banking application is rebuilt using SQLite.<br>
Instead of storing data in CSV files, data is stored in **database tables**.<br>

*A final conclusion note*<br>
At first, storing data in files felt simple enough. Then I tried building a banking system and realized I was slowly becoming the database myself—checking balances, maintaining records, preventing mistakes, and hoping nothing crashed midway. A DBMS takes over these responsibilities, allowing the application to focus on business logic while the database handles data safely and efficiently. That's when the question changed from "Why use a database?" to "Why wouldn't you?
<br>

**Be curious enough to walk beyond the theory**.<br>
The real lessons are often hidden behind the diagrams,definitions, and formulas. Sometimes, understanding begins only when you build, break, question, and rebuild.
<br>
**May this case study encourage you to look beneath the surface and discover the "why" behind the "what."**
<br>
With curiosity and a love for learning,<br>
**— Deepti Sree**