from sqlalchemy import create_engine, text 
from flask import flash, redirect, render_template

import os

db_connection_string = os.environ["DB_CONNECTION_STRING"]

engine = create_engine(db_connection_string, connect_args={
  "ssl":{
    "ssl_ca":"/etc/ssl/cert.pem"
  }
})


def add_patient_to_database(name, address, DOB, contact_info):
  with engine.connect() as conn :
    
    query = text("INSERT INTO patient(name, address, DOB,contact_info)VALUES(:name, :address, :DOB, :contact_info)")
    conn.execute(query, {"name":name, "address":address, "DOB":DOB, "contact_info":contact_info})
    flash('patient details added succesfully')
    return render_template('success.html') 
    
    
    

    
    
  





  






  
    


  
  
  


