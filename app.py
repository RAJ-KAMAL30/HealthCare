from flask import Flask , render_template , request , flash , redirect
from flask_sqlalchemy import SQLAlchemy
from database import add_patient_to_database
from database import add_medicalHistory_to_database
from database import add_prescription_to_database
from database import add_lab_results_to_database
from database import display_patients

import os

app=Flask(__name__)

app.secret_key = 'dont tell anyone'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_CONNECTION_STRING']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def hello_home():
  return render_template('Home.html')

@app.route("/displayPatients")
def display():
  return display_patients()

@app.route('/patients', methods=['GET','POST'])
def submit_patient():
  if request.method =='POST':
    name = request.form['name']
    address = request.form['address']
    DOB = request.form['DOB']
    contact_info = request.form['contact_info']
    
    add_patient_to_database(name, address, DOB, contact_info)

  return render_template('patients.html')  


@app.route('/MedicalHistory', methods= ['GET','POST'])
def submit_medical_history():
  if request.method =='POST':
    diagnosis = request.form['diagnosis'];
    p_id = request.form['p_id']
    treatment = request.form['treatment']
    surgeries = request.form['surgeries']
    medications = request.form['medications']


    add_medicalHistory_to_database(diagnosis, p_id, treatment, surgeries, medications)
    

  return render_template('medicalHistory.html')


@app.route('/Prescription', methods= ['GET','POST'])
def submit_prescription_details():
  if request.method =='POST':
    p_id = request.form['p_id']
    medication_name = request.form['medication_name']
    dosage = request.form['dosage']
    frequency = request.form['frequency']

    add_prescription_to_database(p_id, medication_name, dosage, frequency)

  return render_template('Prescription.html')

    
@app.route('/labResults', methods=['GET','POST'])
def submit_lab_results():
  if request.method=='POST':
    blood_tests = request.form['blood_tests']
    urine_test = request.form['urine_test']
    imaging_test = request.form['imaging_test']
    p_id = request.form['p_id']

    add_lab_results_to_database(blood_tests, urine_test,imaging_test, p_id)
    
    

  return render_template('labResults.html')
    

  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)