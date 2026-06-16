Case Study : A Bank Transaction
<br>
**Banking Transaction System**<br>
Consider a simple banking system where a person can open a new account, transfer fund to an existing account and check the history of all her transactions till date.

The application performs the following checks:<br>
**-**If the account balance is not enough it will not allow the fund transfer.<br>
**-**If the account numbers are not correct, it will flash a message and terminate the transaction.<br>
**-**If a transaction is successful, it prints a confirmation message<br>

We will use this banking transaction system to compare various features of a file-based implementation vs a DBMS-based implementation.<br>

*File-based Implementation*<br>
**-**Account details stored in accounts.csv
**-**Transaction details stored in ledger.csv