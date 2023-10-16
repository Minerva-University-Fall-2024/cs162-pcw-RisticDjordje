CREATE TABLE Users (
    userID INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    role TEXT NOT NULL
);

CREATE TABLE Courses (
    courseID INTEGER PRIMARY KEY,
    courseName TEXT NOT NULL,
    instructorID INTEGER,
    FOREIGN KEY (instructorID) REFERENCES Users(userID)
);

CREATE TABLE Enrollments (
    enrollmentID INTEGER PRIMARY KEY,
    userID INTEGER,
    courseID INTEGER,
    grade REAL,
    FOREIGN KEY (userID) REFERENCES Users(userID),
    FOREIGN KEY (courseID) REFERENCES Courses(courseID)
);


INSERT INTO Users (username, password, email, role)
VALUES ('JohnDoe', 'password123', 'johndoe@email.com', 'student');

INSERT INTO Users (username, password, email, role)
VALUES ('JaneSmith', 'password456', 'janesmith@email.com', 'instructor');

INSERT INTO Courses (courseName, instructorID)
VALUES ('Math 101', 2);

INSERT INTO Enrollments (userID, courseID, grade)
VALUES (1, 1, NULL);

-- More users
INSERT INTO Users (username, password, email, role)
VALUES ('AlanTuring', 'enigma789', 'alan@email.com', 'student');

INSERT INTO Users (username, password, email, role)
VALUES ('GraceHopper', 'bugfix101', 'grace@email.com', 'instructor');

-- More courses
INSERT INTO Courses (courseName, instructorID)
VALUES ('Computer Science 101', 4);

INSERT INTO Courses (courseName, instructorID)
VALUES ('Programming Basics', 4);

-- More enrollments
INSERT INTO Enrollments (userID, courseID, grade)
VALUES (3, 2, NULL);
INSERT INTO Enrollments (userID, courseID, grade)
VALUES (3, 3, NULL);
INSERT INTO Enrollments (userID, courseID, grade)
VALUES (1, 2, NULL);
INSERT INTO Enrollments (userID, courseID, grade)
VALUES (1, 3, NULL);


BEGIN TRANSACTION;

-- Add new student
INSERT INTO Users (username, password, email, role)
VALUES ('AdaLovelace', 'algorithm456', 'ada@email.com', 'student');

-- Enroll new student in 'Programming Basics' using the last_insert_rowid() directly
INSERT INTO Enrollments (userID, courseID, grade)
VALUES (last_insert_rowid(), 3, NULL);

-- Assign Grace Hopper as the instructor for 'Programming Basics'
UPDATE Courses SET instructorID = 4 WHERE courseName = 'Programming Basics';

COMMIT;


-- Transaction 2
BEGIN TRANSACTION;

UPDATE Enrollments SET grade = 85 WHERE enrollmentID = 1;

SELECT AVG(grade) AS AverageGrade
FROM Enrollments
WHERE courseID = (SELECT courseID FROM Courses WHERE courseName = 'Math 101');

COMMIT;


-- Move Alan Turing to 'Programming Basics'
BEGIN TRANSACTION;

UPDATE Enrollments SET courseID = 3 WHERE userID = 3 AND courseID = 2;

COMMIT;
