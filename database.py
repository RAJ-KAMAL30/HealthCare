from sqlalchemy import create_engine, text
from flask_sqlalchemy import SQLAlchemy
from flask import flash, redirect, render_template , request , url_for
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


def add_Outcomes_to_database(p_id,readmission_rates, medical_adherance):
  with engine.connect() as conn :
    query=text("INSERT INTO Outcomes(p_id, readmission_rates, medical_adherance)VALUES(:p_id, :readmission_rates, :medical_adherance)")
    conn.execute(query,{"p_id":p_id, "readmission_rates":readmission_rates, "medical_adherance":medical_adherance})

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


def display_prescription():
  with engine.connect() as connection:
    query = text("SELECT * from prescription")
    result = connection.execute(query)
    prescription = []
    for row in result :
      prescription_detail = {
        "p_id":row[0],
        "medication_name":row[1],
        "dosage":row[2],
        "frequency":row[3]
      }
      prescription.append(prescription_detail)

    return render_template("display_prescription_detail.html", prescription = prescription )


def display_lab_results():
  with engine.connect() as connection:
    query = text("SELECT * from lab_results")
    result = connection.execute(query) 
    lab_results = []
    for row in result:
      lab_result_detail ={
        "blood_tests":row[0],
        "urine_test":row[1],
        "imaging_test":row[2],
        "p_id":row[3]
      }
      lab_results.append(lab_result_detail)

    return render_template('display_lab_result_details.html', lab_results = lab_results)


def update_patient(p_id):
  with engine.connect() as conn :
    query = text("SELECT * FROM patient WHERE p_id = :p_id")
    result = conn.execute(query , {'p_id': p_id})
    patient = result.fetchone()

  if patient is None :
    return "Patient not found"

  if request.method == 'POST':
    name = request.form['name']
    address= request.form['address']
    DOB = request.form['DOB']
    contact_info = request.form['contact_info']

    with engine.connect() as connection :
      query = text("UPDATE patient SET name = :name, address = :address, DOB = :DOB, contact_info = :contact_info WHERE p_id = :p_id")
      connection.execute(query ,{"name":name, "address":address, "DOB":DOB, "contact_info":contact_info, "p_id":p_id})

    return redirect('/displayPatients')
    
  return render_template('update_patient.html', patient = patient)


def update_medicalHistory(record_id):
  with engine.connect() as conn :
    query = text("SELECT * FROM medicalHistory WHERE record_id = :record_id")
    result = conn.execute(query , {'record_id': record_id})
    medicalHistory = result.fetchone()

  if medicalHistory is None :
    return "Patient not found"

  if request.method == 'POST':
    diagnosis = request.form['diagnosis']
    p_id = request.form['p_id']
    treatment = request.form['treatment']
    surgeries = request.form['surgeries']
    medications = request.form['medications']
    
    with engine.connect() as connection :
      query = text("UPDATE medicalHistory SET diagnosis = :diagnosis, p_id = :p_id, treatment = :treatment, surgeries = :surgeries , medications = :medications WHERE record_id = :record_id")
      connection.execute(query ,{"diagnosis":diagnosis, "p_id":p_id, "treatment":treatment, "surgeries":surgeries, "medications":medications, "record_id":record_id })

    return redirect('/displayMedicalHistory')
    
  return render_template('update_medicalHistory.html', medicalHistory = medicalHistory )
    

def update_prescription(p_id):
  with engine.connect() as conn :
    query = text("SELECT * FROM prescription WHERE p_id = :p_id")
    result = conn.execute(query , {'p_id': p_id})
    prescription = result.fetchone()

  if prescription is None :
    return "Patient not found"

  if request.method == 'POST':
    medication_name = request.form['medication_name']
    dosage = request.form['dosage']
    frequency = request.form['frequency']
    
    
    with engine.connect() as connection :
      query = text("UPDATE prescription SET medication_name = :medication_name, dosage = :dosage, frequency = :frequency  WHERE p_id = :p_id")
      connection.execute(query ,{"medication_name":medication_name, "dosage":dosage, "frequency":frequency, "p_id":p_id })

    return redirect("/displayPrescription")
    
  return render_template('update_prescription.html', prescription = prescription )


def update_lab_results(p_id):
  with engine.connect() as conn:
    query = text("SELECT * FROM lab_results WHERE p_id = :p_id")
    result = conn.execute(query , {'p_id': p_id})
    lab_results = result.fetchone()
    
      

    if lab_results is None :
      return "Patient not found"
      
    

  if request.method == 'POST':
    blood_tests = request.form['blood_tests']
    urine_test = request.form["urine_test"]
    imaging_test = request.form["imaging_test"]
    
    
    with engine.connect() as connection :
      query = text("UPDATE lab_results SET blood_tests = :blood_tests, urine_test = :urine_test, imaging_test = :imaging_test  WHERE p_id = :p_id")
      connection.execute(query ,{"blood_tests":blood_tests, "urinr_test":urine_test, "imaging_test":imaging_test, "p_id":p_id })

    return redirect("/displayLabResults")
    
  return render_template('update_lab_results.html', lab_results = lab_results )
    
    
    
  

   
    
   
   
  

   
      
      

    
    

    
    
  





  






  
    


  
  
  


