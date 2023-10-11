CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY,
    FirstName TEXT,
    LastName TEXT,
    Email TEXT UNIQUE
);

CREATE TABLE Classes (
    ClassID INTEGER PRIMARY KEY,
    ClassName TEXT,
    Instructor TEXT,
    Schedule DATETIME,
    Capacity INTEGER
);

CREATE TABLE Bookings (
    BookingID INTEGER PRIMARY KEY,
    UserID INTEGER,
    ClassID INTEGER,
    BookingTime DATETIME,
    FOREIGN KEY (UserID) REFERENCES Users (UserID),
    FOREIGN KEY (ClassID) REFERENCES Classes (ClassID)
);

CREATE TABLE Attendance (
    AttendanceID INTEGER PRIMARY KEY,
    ClassID INTEGER,
    UserID INTEGER,
    CheckInTime DATETIME,
    FOREIGN KEY (ClassID) REFERENCES Classes (ClassID),
    FOREIGN KEY (UserID) REFERENCES Users (UserID)
);

-- INSERT DATA

-- Insert data into USERS
INSERT INTO Users (FirstName, LastName, Email) VALUES ('Sarah', 'Williams', 'sarah@example.com');
INSERT INTO Users (FirstName, LastName, Email) VALUES ('Michael', 'Brown', 'michael@example.com');
INSERT INTO Users (FirstName, LastName, Email) VALUES ('John', 'Smith', 'john@example.com');
INSERT INTO Users (FirstName, LastName, Email) VALUES ('Jane', 'Doe', 'jane@example.com');
INSERT INTO Users (FirstName, LastName, Email) VALUES ('Mike', 'Johnson', 'mike@example.com');

-- Insert data into the Classes table
INSERT INTO Classes (ClassName, Instructor, Schedule, Capacity) VALUES ('Yoga Class', 'Anna', '2023-10-12 08:00:00', 20);
INSERT INTO Classes (ClassName, Instructor, Schedule, Capacity) VALUES ('Spin Class', 'David', '2023-10-14 10:00:00', 15);
INSERT INTO Classes (ClassName, Instructor, Schedule, Capacity) VALUES ('Zumba Class', 'Sarah', '2023-10-16 18:30:00', 25);
INSERT INTO Classes (ClassName, Instructor, Schedule, Capacity) VALUES ('Pilates Class', 'Emily', '2023-10-13 12:30:00', 18);
INSERT INTO Classes (ClassName, Instructor, Schedule, Capacity) VALUES ('CrossFit Class', 'James', '2023-10-15 17:00:00', 30);

-- Insert data into the Bookings table
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (1, 1, '2023-10-11 15:00:00');
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (2, 2, '2023-10-11 16:30:00');
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (3, 1, '2023-10-12 07:45:00');
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (4, 3, '2023-10-15 08:15:00');
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (1, 2, '2023-10-15 09:30:00');
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (2, 4, '2023-10-15 15:45:00');
INSERT INTO Bookings (UserID, ClassID, BookingTime) VALUES (3, 5, '2023-10-15 16:30:00');

-- Insert data into the Attendance table
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (1, 1, '2023-10-12 07:55:00');
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (2, 2, '2023-10-14 10:05:00');
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (1, 3, '2023-10-12 07:58:00');
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (3, 4, '2023-10-15 08:10:00');
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (2, 1, '2023-10-15 09:35:00');
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (4, 2, '2023-10-15 15:50:00');
INSERT INTO Attendance (ClassID, UserID, CheckInTime) VALUES (5, 3, '2023-10-15 16:35:00');

-- QUERY DATA

-- Who has booked the "Yoga Class" on 2023-10-12?
SELECT Users.FirstName, Users.LastName
FROM Users
JOIN Bookings ON Users.UserID = Bookings.UserID
JOIN Classes ON Bookings.ClassID = Classes.ClassID
WHERE Classes.ClassName = 'Yoga Class' AND Classes.Schedule = '2023-10-12 08:00:00';

-- How many bookings have been made for the "Zumba Class"?
SELECT COUNT(*) AS TotalBookings
FROM Bookings
WHERE ClassID = (SELECT ClassID FROM Classes WHERE ClassName = 'Zumba Class');

-- List the users who attended "Spin Class" on 2023-10-14.
SELECT Users.FirstName, Users.LastName
FROM Users
JOIN Attendance ON Users.UserID = Attendance.UserID
JOIN Classes ON Attendance.ClassID = Classes.ClassID
WHERE Classes.ClassName = 'Spin Class' AND Classes.Schedule = '2023-10-14 10:00:00';

-- How many users attended each class on 2023-10-15?
SELECT Classes.ClassName, COUNT(*) AS TotalAttendees
FROM Classes
JOIN Attendance ON Classes.ClassID = Attendance.ClassID
WHERE Attendance.CheckInTime LIKE '2023-10-15%'
GROUP BY Classes.ClassName;

