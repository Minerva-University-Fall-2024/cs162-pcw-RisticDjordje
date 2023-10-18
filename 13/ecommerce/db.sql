CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

-- Sample data for Customers
INSERT INTO Customers (CustomerID, Name, Email, Phone, Address)
VALUES
    (1, 'John Doe', 'johndoe@email.com', '123-456-7890', '123 Main St'),
    (2, 'Jane Smith', 'janesmith@email.com', '987-654-3210', '456 Elm St'),
    (3, 'Alice Johnson', 'alice@email.com', '555-123-4567', '789 Oak Ave');

 CREATE TABLE SupportTickets (
    TicketID INT PRIMARY KEY,
    CustomerID INT,
    Subject VARCHAR(255),
    Description TEXT,
    Status VARCHAR(20),
    CreatedAt TIMESTAMP,
    UpdatedAt TIMESTAMP,
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Sample data for SupportTickets
INSERT INTO SupportTickets (TicketID, CustomerID, Subject, Description, Status, CreatedAt, UpdatedAt)
VALUES
    (1, 1, 'Issue with Order #12345', 'I received the wrong product in my order.', 'Open', '2023-10-01 09:00:00', '2023-10-01 09:00:00'),
    (2, 2, 'Missing Items in Order #54321', 'Some items from my order are missing.', 'Open', '2023-10-02 10:30:00', '2023-10-02 10:30:00'),
    (3, 1, 'Refund Request for Order #67890', 'I would like to request a refund for my order.', 'Open', '2023-10-03 14:15:00', '2023-10-03 14:15:00');


CREATE TABLE TicketReplies (
    ReplyID INT PRIMARY KEY,
    TicketID INT,
    CustomerID INT,
    Message TEXT,
    CreatedAt TIMESTAMP,
    FOREIGN KEY (TicketID) REFERENCES SupportTickets(TicketID),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
);

-- Sample data for TicketReplies
INSERT INTO TicketReplies (ReplyID, TicketID, CustomerID, Message, CreatedAt)
VALUES
    (1, 1, 1, 'I apologize for the inconvenience. We will ship the correct product to you immediately.', '2023-10-01 10:00:00'),
    (2, 1, 1, 'Thank you for your prompt response!', '2023-10-01 11:30:00'),
    (3, 2, 2, 'We are investigating the issue and will resolve it as soon as possible.', '2023-10-02 11:00:00');


CREATE TABLE Products (
    ProductID INT PRIMARY KEY,
    Name VARCHAR(255),
    CategoryID INT,
    Price DECIMAL(10, 2),
    Description TEXT,
    FOREIGN KEY (CategoryID) REFERENCES ProductCategories(CategoryID)
);

-- Sample data for Products
INSERT INTO Products (ProductID, Name, CategoryID, Price, Description)
VALUES
    (1, 'Smartphone', 1, 499.99, 'The latest model with advanced features.'),
    (2, 'Laptop', 2, 899.99, 'Powerful and lightweight laptop for professionals.'),
    (3, 'Headphones', 3, 149.99, 'High-quality wireless headphones with noise-cancellation.');

CREATE TABLE ProductCategories (
    CategoryID INT PRIMARY KEY,
    Name VARCHAR(50)
);

-- Sample data for ProductCategories
INSERT INTO ProductCategories (CategoryID, Name)
VALUES
    (1, 'Electronics'),
    (2, 'Computers'),
    (3, 'Audio');


-- Admin Query 1: How many open support tickets are there?
SELECT COUNT(*) AS OpenTickets
FROM SupportTickets
WHERE Status = 'Open';



-- Admin Query 2: List the most recently created support tickets.
SELECT TicketID, Subject, Status, CreatedAt
FROM SupportTickets
ORDER BY CreatedAt DESC
LIMIT 5;


-- Admin Query 3: List the most recently updated support tickets.
SELECT TicketID, Subject, Status, UpdatedAt
FROM SupportTickets
ORDER BY UpdatedAt DESC
LIMIT 5;

