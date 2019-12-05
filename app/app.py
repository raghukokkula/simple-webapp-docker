import os
import mysql.connector
from flask import Flask
app = Flask(__name__)

@app.route("/")
def main():
    return "Welcome!"

@app.route('/how are you')
def hello():
    return 'I am good, how about you?'

@app.route('/read from database')
def read():
    config = {
        'user': 'root',
        'password': 'root',
        'host': 'db',
        'port': '3306',
        'database': 'employee_db'
    }
    connection = mysql.connector.connect(**config)
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM employees")
    row = cursor.fetchone()
    result = []
    while row is not None:
      result.append(row[0])
      row = cursor.fetchone()

    cursor.close()
    connection.close()

    return ",".join(result)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
