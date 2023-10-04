PRAGMA foreign_keys = ON;

-- Users table
CREATE TABLE Users (
    user_id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    email TEXT NOT NULL
);

-- Accounts table
CREATE TABLE Accounts (
    account_id INTEGER PRIMARY KEY,
    user_id INTEGER NOT NULL,
    account_name TEXT NOT NULL,
    balance REAL NOT NULL,
    FOREIGN KEY (user_id) REFERENCES Users(user_id)
);

-- Transactions table
CREATE TABLE Transactions (
    transaction_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    transaction_date DATE NOT NULL,
    description TEXT NOT NULL,
    amount REAL NOT NULL,
    FOREIGN KEY (account_id) REFERENCES Accounts(account_id)
);


-- Users
INSERT INTO Users (username, email) VALUES
    ('user1', 'user1@example.com'),
    ('user2', 'user2@example.com');

-- Accounts
INSERT INTO Accounts (user_id, account_name, balance) VALUES
    (1, 'Savings', 5000.00),
    (2, 'Checking', 2500.00);

-- Transactions
INSERT INTO Transactions (account_id, transaction_date, description, amount) VALUES
    (1, '2023-09-01', 'Salary', 3000.00),
    (1, '2023-09-05', 'Groceries', -100.00),
    (2, '2023-09-03', 'Rent', -1200.00);


-- Query 1 : Get the balance of the Savings account for user 1
SELECT balance
FROM Accounts
WHERE user_id = 1 AND account_name = 'Savings';

-- Query 2 : Get the total amount of all transactions for account 1
SELECT SUM(amount)
FROM Transactions
WHERE account_id = 1;

-- Query 3 : Get the total amount of all transactions for user 1 across all accounts (Savings and Checking) 
SELECT account_name, SUM(amount)
FROM Transactions
JOIN Accounts ON Transactions.account_id = Accounts.account_id
WHERE user_id = 1
GROUP BY account_name;

-- Query 4 : How much did user2 spend on transactions in September 2023?
SELECT SUM(amount) AS total_spent
FROM Transactions
WHERE account_id IN (SELECT account_id FROM Accounts WHERE user_id = 2)
AND transaction_date BETWEEN '2023-09-01' AND '2023-09-30';

-- Query 5 : How much did user1 spend on transactions in September 2023?
SELECT *
FROM Transactions
ORDER BY amount 
LIMIT 2;

--Query 6: Show entire table for Transactions
SELECT *
FROM Transactions;
