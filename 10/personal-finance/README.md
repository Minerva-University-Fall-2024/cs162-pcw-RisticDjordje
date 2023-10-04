# Database Schema and Queries Explanation

This README provides a detailed explanation of the SQL code for a Personal Finance Management App. The code includes table creation, data insertion, and SQL queries. The README will guide you through each part of the code and its purpose.

## Enabling Foreign Key Constraints

Before defining the database schema, foreign key constraints are enabled using the following PRAGMA statement:
PRAGMA foreign_keys = ON;


This statement enables foreign key constraints in SQLite, ensuring referential integrity when defining relationships between tables.

## Database Schema

### Users Table
The `Users` table stores information about app users. It includes the following columns:
- `user_id`: An integer representing the unique user ID (Primary Key).
- `username`: Text field for the user's username.
- `email`: Text field for the user's email address.

### Accounts Table
The `Accounts` table stores information about user accounts. It includes the following columns:
- `account_id`: An integer representing the unique account ID (Primary Key).
- `user_id`: Integer representing the user who owns the account (Foreign Key referencing `Users` table).
- `account_name`: Text field for the account name.
- `balance`: Real number representing the account balance.

### Transactions Table
The `Transactions` table stores information about financial transactions. It includes the following columns:
- `transaction_id`: An integer representing the unique transaction ID (Primary Key).
- `account_id`: Integer representing the account involved in the transaction (Foreign Key referencing `Accounts` table).
- `transaction_date`: Date of the transaction.
- `description`: Text field describing the transaction.
- `amount`: Real number representing the transaction amount.

## Data Insertion

- Data is inserted into the `Users`, `Accounts`, and `Transactions` tables to populate the database with sample information. Users, accounts, and transactions are added with relevant data.

## SQL Queries

### Query 1: Get the balance of the Savings account for user 1
This query retrieves the balance of the "Savings" account for user 1. It filters accounts by `user_id` and `account_name`.

### Query 2: Get the total amount of all transactions for account 1
This query calculates the total amount of all transactions for account 1. It filters transactions by `account_id`.

### Query 3: Get the total amount of all transactions for user 1 across all accounts (Savings and Checking)
This query calculates the total transaction amounts for user 1 across all accounts. It involves joining the `Transactions` and `Accounts` tables and grouping the results by account name.

### Query 4: How much did user2 spend on transactions in September 2023?
This query calculates the total amount spent by user2 on transactions in September 2023. It filters transactions by `user_id` and `transaction_date`.

### Query 5: How much did user1 spend on transactions in September 2023?
This query retrieves the two transactions with the highest amounts for user1 in September 2023. It orders transactions by amount in descending order and limits the result to the top 2 records.

### Query 6: Show the entire table for Transactions
This query retrieves and displays all records from the `Transactions` table, showing the entire transaction history.
