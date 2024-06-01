from sqlalchemy import create_engine, Column, Integer, String, Boolean,Text,Unicode
from sqlalchemy.orm import declarative_base, sessionmaker

# Connection string with proper driver name
connection_string = (
    "mssql+pyodbc://zahra:zahra@DESKTOP-S5PAQ60/DBfirstcode?"
    "driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
)

# Create the SQLAlchemy engine
engine = create_engine(connection_string, echo=True)

# Define the base class for the models using the updated import path
Base = declarative_base()


# Example model definition
class personnel(Base):
    __tablename__ = 'personnel'
    id = Column(Integer, primary_key=True)
    name = Column(Unicode(100))
    family = Column(Unicode(100))
    age = Column(Integer)
    sex = Column(Boolean)
    def __init__(self,name="", family="", age=0, sex=True):
        self.name = name
        self.family = family
        self.age = age
        self.sex = sex


# Create all tables
try:
    Base.metadata.create_all(engine)
    print("Tables created successfully!")
except Exception as e:
    print(f"Error occurred while creating tables: {e}")

# Create a new session
Session = sessionmaker(bind=engine)
session = Session()

