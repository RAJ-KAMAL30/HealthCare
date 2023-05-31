from flask import Flask , render_template

app=Flask(__name__)

@app.route("/")
def hello_kamal():
  return render_template('Home.html')
  
@app.route('/patients')
def patients():
    return render_template('patients.html')
  
if __name__ == "__main__":
  app.run(host='0.0.0.0',debug=True)