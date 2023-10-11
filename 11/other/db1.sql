-- Create the Books table
CREATE TABLE Books (
    ISBN TEXT PRIMARY KEY,
    Title TEXT,
    AuthorID INTEGER,
    Price REAL,
    PublishedYear INTEGER,
    Genre TEXT
);

-- Create the Authors table
CREATE TABLE Authors (
    AuthorID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT
);

-- Create the Customers table
CREATE TABLE Customers (
    CustomerID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT UNIQUE
);

-- Create the Orders table
CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY,
    CustomerID INTEGER,
    OrderDate DATETIME,
    TotalAmount REAL,
    FOREIGN KEY (CustomerID) REFERENCES Customers (CustomerID)
);

-- Create the OrderDetails table
CREATE TABLE OrderDetails (
    OrderDetailID INTEGER PRIMARY KEY,
    OrderID INTEGER,
    ISBN TEXT,
    Quantity INTEGER,
    FOREIGN KEY (OrderID) REFERENCES Orders (OrderID),
    FOREIGN KEY (ISBN) REFERENCES Books (ISBN)
);

-- Create the Inventory table
CREATE TABLE Inventory (
    ISBN TEXT PRIMARY KEY,
    StockQuantity INTEGER
);


INSERT INTO Authors (FirstName, LastName) VALUES ('John', 'Doe');
INSERT INTO Authors (FirstName, LastName) VALUES ('Jane', 'Smith');
INSERT INTO Authors (FirstName, LastName) VALUES ('David', 'Johnson');

INSERT INTO Books (ISBN, Title, AuthorID, Price, PublishedYear, Genre) VALUES ('978-1234567890', 'The Book Title', 1, 24.99, 2020, 'Fiction');
INSERT INTO Books (ISBN, Title, AuthorID, Price, PublishedYear, Genre) VALUES ('978-0987654321', 'Another Book', 2, 19.99, 2018, 'Mystery');

INSERT INTO Customers (FirstName, LastName, Email) VALUES ('Alice', 'Johnson', 'alice@example.com');
INSERT INTO Customers (FirstName, LastName, Email) VALUES ('Bob', 'Smith', 'bob@example.com');

INSERT INTO Inventory (ISBN, StockQuantity) VALUES ('978-1234567890', 50);
INSERT INTO Inventory (ISBN, StockQuantity) VALUES ('978-0987654321', 30);

SELECT Books.Title
FROM Books
JOIN Authors ON Books.AuthorID = Authors.AuthorID
WHERE Authors.FirstName = 'John' AND Authors.LastName = 'Doe';

SELECT SUM(Orders.TotalAmount) AS TotalSales
FROM Orders
JOIN Customers ON Orders.CustomerID = Customers.CustomerID
WHERE Customers.FirstName = 'Alice' AND Customers.LastName = 'Johnson';

SELECT Inventory.StockQuantity
FROM Inventory
WHERE Inventory.ISBN = '978-1234567890';
