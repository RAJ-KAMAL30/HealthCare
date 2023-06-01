from flask import Flask , render_template , request , flash , redirect
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://7tmswmutzfmcdyj0ggsq:pscale_pw_anJnenu1qn0tzXCgxtJgQs9MdozFFKPq0oqASd2aGP:aws.connect.psdb.cloud/heathcare'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class patient(db.Model):
    p_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(100),nullable=False)
    DOB = db.Column(db.String(20),nullable=False)
    contact_info = db.Column(db.String(25),nullable=False)
  
@app.route("/")
def hello_home():
  return render_template('Home.html')
  

@app.route('/patients', methods=['GET', 'POST'])
def add_patient():
    if request.method == 'POST':
        name = request.form['name']
        address = request.form['address']
        DOB = request.form['DOB']
        contact_info = request.form['contact_info']
      
        patient = patient(name=name, address=address, DOB=DOB, contact_info=contact_info)
        db.session.add(patient)
        db.session.commit()
      
        flash('Patient details added successfully!', 'success')
        return redirect('/patients')

    else:
      return render_template('patients.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)