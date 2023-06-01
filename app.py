from flask import Flask , render_template , request , flash , redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine 

import os



app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.environ['DB_CONNECTION_STRING']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

database_connection_string = os.environ['DB_CONNECTION_STRING']

engine = create_engine(database_connection_string,connect_args={
        "ssl": {
          "ssl_ca": "/etc/ssl/cert.pem"
        }})

db=SQLAlchemy(app)

class Patient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100))
    DOB = db.Column(db.String(20))
    contact_info = db.Column(db.String(25))

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
    
    patient = Patient(name=name, address=address, DOB=DOB,contact_info=contact_info)     

    db.session.add(patient)
    db.session.commit()

    flash('patient details added succesfully','success')
    return redirect('/patients')

  return render_template('patients.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)