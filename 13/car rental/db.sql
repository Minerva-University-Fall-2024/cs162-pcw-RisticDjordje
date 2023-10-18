-- Create the Customers Table
CREATE TABLE Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Email VARCHAR(255),
    Phone VARCHAR(20),
    Address VARCHAR(255)
);

-- Create the Vehicles Table
CREATE TABLE Vehicles (
    VehicleID INT PRIMARY KEY,
    Make VARCHAR(50),
    Model VARCHAR(50),
    Year INT,
    LicensePlate VARCHAR(15),
    CurrentStatus VARCHAR(20),
    RentalPrice DECIMAL(10, 2)
);

-- Create the Rentals Table
CREATE TABLE Rentals (
    RentalID INT PRIMARY KEY,
    CustomerID INT,
    VehicleID INT,
    RentalStartDate DATE,
    RentalEndDate DATE,
    TotalCost DECIMAL(10, 2),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);

-- Create the Maintenance Table
CREATE TABLE Maintenance (
    MaintenanceID INT PRIMARY KEY,
    VehicleID INT,
    MaintenanceType VARCHAR(50),
    MaintenanceDate DATE,
    Cost DECIMAL(10, 2),
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);


INSERT INTO Customers (CustomerID, Name, Email, Phone, Address)
VALUES
    (1, 'John Doe', 'johndoe@email.com', '123-456-7890', '123 Main St'),
    (2, 'Jane Smith', 'janesmith@email.com', '987-654-3210', '456 Elm St'),
    (3, 'Alice Johnson', 'alice@email.com', '555-123-4567', '789 Oak Ave'),
    (4, 'Bob Wilson', 'bob@email.com', '333-555-7777', '101 Pine Rd'),
    (5, 'Eva Davis', 'eva@email.com', '222-888-9999', '246 Cedar Ln'),
    (6, 'Michael Lee', 'michael@email.com', '444-777-1111', '567 Birch Blvd'),
    (7, 'Olivia White', 'olivia@email.com', '111-222-3333', '890 Red St'),
    (8, 'Sophia Brown', 'sophia@email.com', '777-888-9999', '345 Green Rd'),
    (9, 'Liam Martin', 'liam@email.com', '999-111-5555', '678 Blue Ln'),
    (10, 'Emma Hall', 'emma@email.com', '666-333-2222', '432 Yellow Ave');

INSERT INTO Vehicles (VehicleID, Make, Model, Year, LicensePlate, CurrentStatus, RentalPrice)
VALUES
    (1, 'Toyota', 'Camry', 2022, 'ABC123', 'Available', 50.00),
    (2, 'Honda', 'Civic', 2021, 'DEF456', 'Available', 45.00),
    (3, 'Ford', 'Escape', 2022, 'GHI789', 'In Maintenance', 60.00),
    (4, 'Chevrolet', 'Malibu', 2022, 'JKL012', 'Available', 55.00),
    (5, 'Nissan', 'Altima', 2020, 'MNO345', 'Rented', 48.00),
    (6, 'Hyundai', 'Elantra', 2021, 'PQR678', 'Available', 47.00),
    (7, 'Kia', 'Soul', 2022, 'STU901', 'Available', 52.00),
    (8, 'Subaru', 'Outback', 2022, 'VWX234', 'Available', 58.00),
    (9, 'Mazda', 'CX-5', 2020, 'YZA567', 'Available', 62.00),
    (10, 'Volkswagen', 'Jetta', 2021, 'BCD890', 'Available', 49.00);

INSERT INTO Rentals (RentalID, CustomerID, VehicleID, RentalStartDate, RentalEndDate, TotalCost)
VALUES
    (1, 1, 5, '2023-01-10', '2023-01-15', 240.00),
    (2, 2, 3, '2023-02-05', '2023-02-12', 420.00),
    (3, 3, 1, '2023-03-20', '2023-03-25', 300.00),
    (4, 4, 7, '2023-04-15', '2023-04-22', 364.00),
    (5, 5, 2, '2023-05-08', '2023-05-15', 315.00),
    (6, 6, 8, '2023-06-02', '2023-06-09', 406.00),
    (7, 7, 10, '2023-07-14', '2023-07-20', 343.00),
    (8, 8, 4, '2023-08-01', '2023-08-10', 495.00),
    (9, 9, 9, '2023-09-18', '2023-09-24', 434.00),
    (10, 10, 6, '2023-10-05', '2023-10-15', 560.00);

INSERT INTO Maintenance (MaintenanceID, VehicleID, MaintenanceType, MaintenanceDate, Cost)
VALUES
    (1, 3, 'Oil Change', '2023-02-10', 80.00),
    (2, 7, 'Tire Rotation', '2023-04-05', 45.00),
    (3, 8, 'Brake Inspection', '2023-05-20', 60.00),
    (4, 1, 'General Inspection', '2023-06-15', 90.00),
    (5, 6, 'Oil Change', '2023-08-05', 80.00),
    (6, 4, 'Tire Replacement', '2023-09-10', 200.00),
    (7, 10, 'Brake Repair', '2023-10-02', 120.00),
    (8, 9, 'General Inspection', '2023-11-15', 90.00),
    (9, 2, 'Tire Rotation', '2023-12-05', 45.00),
    (10, 5, 'Oil Change', '2024-01-20', 80.00);

-- How many customer are currently registered in the system?
SELECT COUNT(*) AS TotalCustomers
FROM Customers;

-- Admin Query 2: List all customers who have rented a car in the last month.
SELECT *
FROM Customers
WHERE CustomerID IN (
    SELECT DISTINCT CustomerID
    FROM Rentals
    WHERE RentalEndDate >= DATE_SUB(CURDATE(), INTERVAL 1 MONTH)
);

-- Admin Query 3: Who are the top 5 customers by the number of rentals they've made?
SELECT C.CustomerID, C.Name, COUNT(R.RentalID) AS TotalRentals
FROM Customers C
LEFT JOIN Rentals R ON C.CustomerID = R.CustomerID
GROUP BY C.CustomerID, C.Name
ORDER BY TotalRentals DESC
LIMIT 5;

-- Customer Query 1: What is my contact information?
-- Note: Replace 'X' with your CustomerID.
SELECT Name, Email, Phone, Address
FROM Customers
WHERE CustomerID = 1;

-- Customer Query 2: How many rentals have I made?
-- Note: Replace 'X' with your CustomerID.
SELECT COUNT(*) AS TotalRentals
FROM Rentals
WHERE CustomerID = 1;

-- Admin Query 4: How many vehicles are currently available for rent?
SELECT COUNT(*) AS AvailableVehicles
FROM Vehicles
WHERE CurrentStatus = 'Available';

-- Admin Query 5: What is the rental price per day for a specific vehicle with a given VehicleID?
-- Note: Replace 'X' with your VehicleID.
SELECT RentalPrice
FROM Vehicles
WHERE VehicleID = 1;

-- Customer Query 3: What is the rental price per day for a specific vehicle with a given VehicleID?
-- Note: Replace 'X' with your VehicleID.
SELECT RentalPrice
FROM Vehicles
WHERE VehicleID = 1;