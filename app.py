# app.py (Flask example)

from flask import Flask, render_template, request, redirect, url_for
import mysql.connector

app = Flask(__name__)

# MySQL database configuration (replace with your actual credentials)
db_config = {
    'host': 'localhost',
    'user': 'aliza',
    'password': 'aliza',
    'database': 'userdata'
}

# Initialize MySQL connection
db_conn = mysql.connector.connect(**db_config)

@app.route('/')
def index():
    return render_template('signin.html')

@app.route('/sign', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Validate credentials against MySQL database
    cursor = db_conn.cursor()
    cursor.execute("SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()

    if user:
        # Successful login
        # You can set a session or issue a token here
        return redirect(url_for('index.html'))
    else:
        # Invalid credentials
        return "Invalid username or password"

@app.route('/index.html')
def dashboard():
    return "Welcome to the dashboard!"

if __name__ == '__main__':
    app.run(debug=True)
