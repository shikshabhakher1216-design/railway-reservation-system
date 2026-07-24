from fastapi import FastAPI

from database import engine, SessionLocal
# update code

from models import Base, Passenger
# update code, as Employee contains the complete table structure defined in
# FastAPI will get to know which tables to create

app = FastAPI()

Base.metadata.create_all(bind = engine)
# Base contains the tables, metadata stores table information, create_all creates the tables,
# and bind = engine connects them with the database

@app.get("/")
def home():

    return{"message": "Database Connected Successfully"}

# create databse session
session = SessionLocal()

# insert data using POST
@app.post("/passenger/{Passenger_id}/{Passenger_Name}/{Train_Name}/{Destination}")
# placeholder means a temporary space reserved for dynamic values, coming from Postman / Swagger
def add_employee(Passenger_id: int, Passenger_Name: str, Train_Name: str, Destination: str):
    # the data coming from the API route should follow these datatypes
    
    passenger = Passenger(Passenger_id = Passenger_id, Passenger_Name = Passenger_Name, Train_Name = Train_Name, Destination = Destination)
    
    session.add(passenger)
    # adds data temporarily

    session.commit()
    # saves data permanently into PostgreSQL

    return {"message": "Passenger Added Successfully"}
# confirmation message

# work flow : Postman -> fastAPI -> SQLAlchemy Session -> PostgreSQL

# fetch data using GET
@app.get("/passenger")
def get_Passenger():

    Passenger = session.query(Passenger).all()

    return Passenger


# update data using PUT
@app.put("/passenger/{Passenger_id}/{new_Passenger_Name}")
def update_Passenger(Passenger_id: int, new_Passenger_Name: str):

    Passenger = session.query(Passenger).filter(Passenger.id == Passenger_id).first()

    Passenger.name = new_Passenger_Name
    # change old value

    session.commit()

    return{"message": " Passenger Updated Successfully"}


# update data using DELETE
@app.delete("/passenger/{Passenger_id}")
def delete_Passenger(Passenger_id: int):

    employee = session.query(Passenger).filter(Passenger.id == Passenger_id).first()

    session.delete(Passenger)
    # remove Passenger

    session.commit()

    return{"message": " Passenger Deleted Successfully"}
