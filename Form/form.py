from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

#database Connection
conn = mysql.connector.connect(
    host = "localhost", 
    user = "root",
    password = "1029384756@123",
    database = "flask_forms"
)

cursor = conn.cursor()

@app.route('/')
def index():
    return render_template('form.html')

@app.route('/submit', methods=['post'])
def submit():
    name = request.form['name']
    email = request.form['email']
    age = request.form['age']
    
    #insert data to database
    cursor.execute("INSERT INTO users (name, email, age) VALUES (%s, %s, %s)", (name,email,age))
    conn.commit()

    return render_template('submission.html', name=name, email=email, age=age)
if __name__ == "__main__":
    app.run(debug=True)

