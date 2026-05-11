from flask import Flask,render_template,request,redirect,url_for,session
import mysql.connector 

app = Flask(__name__)
app.secret_key='awkdakwdjakwdkadkajcwadawdaqc'

conn = mysql.connector.connect(
    host='localhost',
    user='root',
    password='1029384756@123',
    database='auth_db'
)

cursor = conn.cursor()

@app.route('/')
def home():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    return "login page"

if __name__ == "__main__":
    app.run(debug=True)