from flask import Flask , render_template , request , flash , redirect
from flask_sqlalchemy import SQLAlchemy
from database import add_patient_to_database

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

  
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)