Case 07 - Database Transactions and ACID Properties

Overview
This project demonstrates how database transactions maintain data consistency during a bank transfer. It uses Python and SQLite to simulate a money transfer between two bank accounts.

Real-World Scenario

A banking application transfer ₹5,000 from Account A to Account B. If an error occurs after deducting money but before crediting the second account, the transaction must be rolled back to prevent money loss.

Concepts Covered
** Database Transactions
** ACID Properties
** COMMIT and ROLLBACK
** Exception Handling
** Data Consistency
** SQLite Database Management

Technologies Used
** Python
** SQLite3

How It Works
1. Create a database containing two bank accounts.
2. Starts a transaction.
3. Deducts money from Account A.
4. Simulates an application error.
5. Rolls back the transaction.
6. Displays the original account balances.

Excepted Result
When an error occurs, the database rolls back all changes and restores the original balances.

Learning Outcome
Learned how database transactions protect financial data and maintain consistency when unexpected errors occur.

