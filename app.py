from databases import *
from flask import Flask, render_template, url_for
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/student/<int:student_id>')
def display_student(student_id):
	student = query_by_id(student_id)
	return render_template('student.html', student=student)

if __name__ == '__main__':
    app.run(debug=True)
