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


def add_prescription_to_database(p_id, medication_name, dosage, frequency):
  with engine.connect() as conn:
    query = text("INSERT INTO prescription(p_id, medication_name, dosage, frequency)VALUES(:p_id, :medication_name, :dosage, :frequency)")
    conn.execute(query, {"p_id":p_id, "medication_name":medication_name, "dosage":dosage, "frequency":frequency})
    flash('Prescription Details added Successfully')
    return render_template('success.html')
    
    
def add_lab_results_to_database(blood_tests, urine_test, imaging_test, p_id):
  with engine.connect() as conn:
    query = text("INSERT INTO lab_results(blood_tests, urine_test, imaging_test, p_id)VALUES(:blood_tests, :urine_test, :imaging_test, :p_id)")
    conn.execute(query, {"blood_tests":blood_tests, "urine_test":urine_test, "imaging_test":imaging_test, "p_id":p_id})
    
    return render_template('success.html')  



def display_patients():
  with engine.connect() as connection :
    query = text("SELECT * from patient")
    result = connection.execute(query)
    patients = []
    for row in result:
      patient = {
        "p_id":row[0],
        "name":row[1],
        "address":row[2],
        "DOB":row[3],
        "contact_info":row[4] 
      }
      patients.append(patient)
  
  return render_template('display_patients.html', patients = patients)    



def display_medical_history():
  with engine.connect() as connection:
    query = text("SELECT * from medicalHistory")
    result = connection.execute(query)
    medicalHistory = []
    for row in result : 
      medical_detail = {
        "record_id":row[0],
        "diagnosis":row[1],
        "p_id": row[2],
        "treatment":row[3],
        "surgeries":row[4], 
        "medications": row[5]
      }
      medicalHistory.append(medical_detail)

  return render_template('display_medical_details.html', medicalHistory=medicalHistory)
    
      
      

    
    

    
    
  





  






  
    


  
  
  


