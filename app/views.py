# views.py

from sqlite3.dbapi2 import SQLITE_DROP_TABLE
from flask import render_template, request, jsonify
import sqlite3 as sql
import os

from app import app

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/about')
def about():
    return render_template("about.html")

@app.route("/students")
def students():
    return render_template("students.html")

@app.route("/i-hate-aidan")
def student_form():
    return render_template("about.html")

@app.route("/test-form")
def test_form():
    return render_template("test_form.html")

@app.route("/process-test-form", methods=['POST'])
def process_test_form():
    email = request.form['email']
    text = "Your email is " + email
    return text

@app.route("/process-student-form-data", methods=["POST"])
def process_student_form_data():
    response = {
        'msg': ''
    }
    if request.method == 'POST':
        try:
            request_data = request.get_json()
            name = request_data['name']
            email_address = request_data['email_address']
            birthday = request_data['birthday']
            subject = request_data['subject']
            response = {
                'message': 'No action taken'
            }
            
            current_dir = os.path.dirname(__file__)
            db_file = os.path.join(current_dir, 'db/database.db')
            con = sql.connect(db_file)
            cur = con.cursor()
            cur.execute("INSERT INTO students (name,email_address,birthday,favorite_subject) VALUES (?,?,?,?)", (name,email_address,birthday,subject))
            con.commit()
            cur.close()
            response['message'] = 'Record successfully added.'
        except:
            con.rollback()
            response['message'] = 'Error inserting'
        finally:
            return jsonify(response)

