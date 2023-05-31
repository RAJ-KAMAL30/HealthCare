from flask import Flask , render_template , request , flash , redirect
import mysql.connector

app=Flask(__name__)
app.secret_key = 'kamal@2230'

@app.route("/")
def hello_home():
  return render_template('Home.html')
  
@app.route('/patients')
def patients():
    return render_template('patients.html')

@app.route('/add_patient', methods=['POST'])
def add_patient():
    name = request.form['name']
    address = request.form['address']
    DOB = request.form['DOB']
    contact_info = request.form['contact_info']
  
    try:
      cnx = mysql.connector.connect(
        host='aws.connect.psdb.cloud',
        user='jq7tk3y78xwwp4mf51bz',
        password='pscale_pw_yZuw6BOWsGcnYceQ7zjUF4XXlUJiIAJLqRPE5bFj7TK',
        database='heathcare'
      )

      cursor = cnx.cursor()
      query = "INSERT INTO patient (name, address, DOB, contact_info) VALUES (%s, %s, %s, %s)"
      values = (name, address, DOB, contact_info)
      cursor.execute(query, values)

      cnx.commit()

      if cursor.rowcount > 0:
            flash('Patient details added successfully!', 'success')
      else:
        flash('An error occurred while adding patient details. Please try again.', 'error')

        # Close the database connection
        cursor.close()
        cnx.close()

        return redirect('/patients')

      flash('Patient details added successfully!', 'success')
      return redirect('/patients')

    except Exception as e:
      flash('An error occurred while adding patient details. Please try again.', 'error')
      return redirect('/patients')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)