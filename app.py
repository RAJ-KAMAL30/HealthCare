from flask import Flask , render_template , request , flash , redirect, session

from database import add_patient_to_database
from database import add_medicalHistory_to_database
from database import add_prescription_to_database
from database import add_lab_results_to_database
from database import display_patients
from database import display_medical_history
from database import display_prescription
from database import display_lab_results
from database import add_Outcomes_to_database
from database import update_patient
from database import update_medicalHistory
from database import update_prescription
from database import update_lab_results

import os

app=Flask(__name__)

app.secret_key = 'dont tell anyone'

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DB_CONNECTION_STRING']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

USER = {
  'healthcare.zone@gmail.com':'HealthCareZone123!'
}
@app.route("/")
def hello_home():
  if 'email' in session :
    return render_template('Home.html', email=session['email'])
  else:
    return redirect('/login')

@app.route('/login', methods = ['GET','POST'])
def login():
  if request.method == 'POST':
    email = request.form['email']
    password = request.form['password']

    if email in USER and password == USER[email]:
      session['email']=email
      return redirect('/')
    else:
      error = "Invalid credentials. PLease try again."
      return render_template('login.html', error=error)

  return render_template('login.html')

@app.route('/logout')
def logout():
  session.clear()
  return redirect('/login')
  

@app.route("/displayPatients")
def display_p():
  return display_patients()

@app.route("/displayMedicalHistory")
def display_m():
  return display_medical_history()

@app.route('/displayPrescription')
def display_pr():
  return display_prescription()

@app.route('/displayLabResults')
def display_l():
  return display_lab_results()


@app.route('/patient/<int:p_id>/update', methods=['GET', 'POST'])
def update_p(p_id):
  return update_patient(p_id)

@app.route("/medicalHistory/<int:record_id>/update", methods=['GET', 'POST'])
def update_m(record_id):
  return update_medicalHistory(record_id)

@app.route("/Prescription/<int:p_id>/update", methods=['GET', 'POST'])
def update_pres(p_id):
  return update_prescription(p_id)

@app.route("/LabResults/<int:p_id>/update", methods=['GET', 'POST'])
def update_lab(p_id):
  return update_lab_results(p_id)

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


@app.route('/Outcomes', methods=['GET','POST'])
def submit_Outcomes():
  if request.method=='POST':
    p_id = request.form['p_id']
    readmission_rates = request.form['readmission_rates']
    medical_adherance = request.form['medical_adherance']
    

    add_Outcomes_to_database(p_id, readmission_rates, medical_adherance)

  return render_template('Outcomes.html')
    

  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)