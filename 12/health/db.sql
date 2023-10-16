CREATE TABLE Patients (
    patientID INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    birthDate TEXT NOT NULL
);

CREATE TABLE Records (
    recordID INTEGER PRIMARY KEY,
    patientID INTEGER,
    visitDate TEXT NOT NULL,
    diagnosis TEXT,
    treatment TEXT,
    FOREIGN KEY (patientID) REFERENCES Patients(patientID)
);

INSERT INTO Patients (name, birthDate)
VALUES ('Robert Brown', '1990-06-15');

INSERT INTO Records (patientID, visitDate, diagnosis, treatment)
VALUES (1, '2023-10-01', 'Flu', 'Rest and Hydration');

INSERT INTO Patients (name, birthDate)
VALUES ('Robert Brown', '1990-06-15');

INSERT INTO Records (patientID, visitDate, diagnosis, treatment)
VALUES (1, '2023-10-01', 'Flu', 'Rest and Hydration');





BEGIN TRANSACTION;

INSERT INTO Records (patientID, visitDate, diagnosis, treatment)
VALUES (1, '2023-10-01', 'Cold', 'Medication and Rest');

SELECT name
FROM Patients p
JOIN Records r ON p.patientID = r.patientID
WHERE r.visitDate = '2023-10-01';

ROLLBACK;


