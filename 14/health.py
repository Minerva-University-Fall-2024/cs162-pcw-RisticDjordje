from sqlalchemy import create_engine, Column, Integer, Text, ForeignKey
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

engine = create_engine('sqlite:///database.db')
Base = declarative_base()

class Patient(Base):
    __tablename__ = 'Patients'
    patientID = Column(Integer, primary_key=True)
    name = Column(Text, nullable=False)
    birthDate = Column(Text, nullable=False)
    records = relationship('Record', back_populates='patient')

class Record(Base):
    __tablename__ = 'Records'
    recordID = Column(Integer, primary_key=True)
    patientID = Column(Integer, ForeignKey('Patients.patientID'), nullable=False)
    visitDate = Column(Text, nullable=False)
    diagnosis = Column(Text)
    treatment = Column(Text)
    patient = relationship('Patient', back_populates='records')

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# Patients
patient1 = Patient(name='Robert Brown', birthDate='1990-06-15')
session.add(patient1)

# Records
record1 = Record(patient=patient1, visitDate='2023-10-01', diagnosis='Flu', treatment='Rest and Hydration')
session.add(record1)

# Commit the transaction
session.commit()

# Begin a SAVEPOINT
savepoint = session.begin_nested()

# Insert another record
record2 = Record(patient=patient1, visitDate='2023-10-01', diagnosis='Cold', treatment='Medication and Rest')
session.add(record2)

# Rollback to the SAVEPOINT
savepoint.rollback()

# Query for patients with visitDate '2023-10-01'
patients_with_visit_date = session.query(Patient.name).join(Record).filter(Record.visitDate == '2023-10-01').all()

# Print the result
print("Patients with visitDate '2023-10-01':", patients_with_visit_date)
