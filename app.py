from flask import Flask , render_template , request , flash , redirect
from flask_sqlalchemy import SQLAlchemy
from database import add_patient_to_database
from database import add_medicalHistory_to_database

import os

app=Flask(__name__)

app.secret_key = 'dont tell anyone'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_CONNECTION_STRING']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

@app.route("/")
def hello_home():
  return render_template('Home.html')

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


    


  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)