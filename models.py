from sqlalchemy import Column, Integer, String
# It is just a table design

from database import Base

class Passenger(Base):

# class used to define structure of table

    __tablename__ = "Passenger"

    Passenger_id = Column(Integer, primary_key= True)

    Passenger_Name = Column(String)

    Train_Name = Column(String)

    Destination = Column(String)
