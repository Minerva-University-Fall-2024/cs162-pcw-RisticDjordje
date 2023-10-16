CREATE TABLE Patients (
    PatientID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(50),
    LastName VARCHAR(50),
    DateOfBirth DATE,
    Gender VARCHAR(10),
    PhoneNumber VARCHAR(20),
    Email VARCHAR(100),
    Address VARCHAR(255)
);


-- 2. MedicalRecords Table
CREATE TABLE MedicalRecords (
    RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    DateRecorded DATE,
    Height FLOAT,
    Weight FLOAT,
    BloodType VARCHAR(5),
    Allergies TEXT,
    CurrentMedications TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);


-- 3. MedicalHistory Table
CREATE TABLE MedicalHistory (
    HistoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    DateOfEvent DATE,
    ConditionName VARCHAR(100),
    TreatmentReceived TEXT,
    Notes TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);


-- 4. Appointments Table
CREATE TABLE Appointments (
    AppointmentID INTEGER PRIMARY KEY AUTOINCREMENT,
    PatientID INTEGER,
    DateOfAppointment DATE,
    TimeOfAppointment TIME,
    DoctorName VARCHAR(100),
    Purpose TEXT,
    Notes TEXT,
    FOREIGN KEY (PatientID) REFERENCES Patients(PatientID)
);

INSERT INTO Patients (FirstName, LastName, DateOfBirth, Gender, PhoneNumber, Email, Address) VALUES 
('John', 'Doe', '1980-05-10', 'Male', '123-456-7890', 'john.doe@email.com', '123 Elm St, Springfield'),
('Jane', 'Smith', '1985-08-15', 'Female', '321-654-0987', 'jane.smith@email.com', '456 Oak St, Springfield'),
('Alice', 'Johnson', '1990-11-20', 'Female', '789-012-3456', 'alice.johnson@email.com', '789 Maple St, Springfield'),
('Bob', 'Brown', '1975-06-25', 'Male', '567-890-1234', 'bob.brown@email.com', '012 Cedar St, Springfield'),
('Charlie', 'Davis', '2000-01-05', 'Male', '345-678-9012', 'charlie.davis@email.com', '345 Birch St, Springfield'),
('Diana', 'White', '1995-04-17', 'Female', '234-567-8901', 'diana.white@email.com', '678 Pine St, Springfield'),
('Ethan', 'Green', '1988-09-30', 'Male', '456-789-0123', 'ethan.green@email.com', '901 Fir St, Springfield'),
('Faye', 'Black', '1983-03-22', 'Female', '678-901-2345', 'faye.black@email.com', '234 Spruce St, Springfield'),
('George', 'Martinez', '1978-07-07', 'Male', '890-123-4567', 'george.martinez@email.com', '567 Redwood St, Springfield'),
('Hannah', 'Lopez', '2005-12-31', 'Female', '123-890-4567', 'hannah.lopez@email.com', '890 Palm St, Springfield');


INSERT INTO MedicalRecords (PatientID, DateRecorded, Height, Weight, BloodType, Allergies, CurrentMedications) VALUES 
(1, '2023-10-10', 175.3, 70.5, 'A+', 'Peanuts', 'Metformin'),
(2, '2023-10-11', 162.5, 55.0, 'B-', 'None', 'Lisinopril'),
(3, '2023-10-12', 168.9, 64.0, 'O+', 'Dairy', 'Atorvastatin'),
(4, '2023-10-13', 180.4, 78.0, 'AB+', 'Shellfish', 'None'),
(5, '2023-10-14', 173.2, 73.0, 'A-', 'Penicillin', 'Amlodipine'),
(6, '2023-10-15', 157.5, 52.5, 'B+', 'None', 'Simvastatin'),
(7, '2023-10-16', 182.8, 81.0, 'O-', 'Gluten', 'Hydrochlorothiazide'),
(8, '2023-10-17', 160.0, 54.0, 'AB-', 'Ibuprofen', 'Gabapentin'),
(9, '2023-10-18', 176.5, 72.0, 'A+', 'None', 'None'),
(10, '2023-10-19', 165.4, 58.5, 'O+', 'Sulfa drugs', 'Losartan');

INSERT INTO MedicalHistory (PatientID, DateOfEvent, ConditionName, TreatmentReceived, Notes) VALUES 
(1, '2020-05-05', 'Hypertension', 'Prescribed medication', 'Stable condition, monitoring'),
(2, '2019-08-15', 'Asthma', 'Inhaler', 'Mild asthma, occasional symptoms'),
(3, '2021-10-20', 'Fracture', 'Cast and physical therapy', 'Full recovery after 3 months'),
(4, '2018-03-10', 'Diabetes', 'Insulin and diet control', 'Regular monitoring required'),
(5, '2022-01-15', 'Allergy', 'Antihistamines', 'Seasonal allergies, especially during spring'),
(6, '2020-11-30', 'Bronchitis', 'Antibiotics', 'Full recovery after 2 weeks'),
(7, '2019-06-07', 'Anemia', 'Iron supplements', 'Condition improved after medication'),
(8, '2021-03-22', 'Migraine', 'Pain relief medication', 'Occasional episodes, stress triggers'),
(9, '2022-04-10', 'Heartburn', 'Antacids', 'Associated with certain foods, dietary adjustments made'),
(10, '2020-12-05',