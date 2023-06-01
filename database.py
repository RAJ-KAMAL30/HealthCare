import sqlalchemy
from sqlalchemy import create_engine , text
from sqlalchemy.orm import sessionmaker
import os

database_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(database_connection_string,connect_args={
        "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
        }})

def add_patient(name, address, dob, contact_info):
  with engine.connect() as conn:
    query = f"INSERT INTO patient(name, address, dob, contact_info) VALUES('{name}', '{address}', '{dob}','{contact_info}')"
                   
    conn.execute(query)

  
    


  
  
  


