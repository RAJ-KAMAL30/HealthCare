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
    flash('patient details added succesfully','success')
    return render_template('success.html') 


def add_medicalHistory_to_database(diagnosis, p_id, treatment, surgeries, medications):
  with engine.connect() as conn:
    query = text("INSERT INTO medicalHistory(diagnosis, p_id, treatment,surgeries,medications)VALUES(:diagnosis,:p_id, :treatment, :surgeries, :medications)")
    conn.execute(query, {"diagnosis":diagnosis, "p_id":p_id, "treatment":treatment, "surgeries":surgeries, "medications":medications})
    flash('Medical History Details added Successfully')
    return render_template('success.html')
    
    
    
    

    
    
  





  






  
    


  
  
  


