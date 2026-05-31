from flask import Flask, render_template, request
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')
@app.route('/python')
def python_questions():
    return render_template('python_questions.html')
@app.route('/java')
def java_questions():
    return render_template('java_questions.html')
@app.route('/sql')
def sql_questions():
    return render_template('sql_questions.html')

@app.route('/hr')
def hr_questions():
    return render_template('hr_questions.html')
@app.route('/mocktest')
def mocktest():
    return render_template('mock_test.html')
@app.route('/result', methods=['POST'])
def result():

    score = 0

    q1 = request.form.get('q1')
    q2 = request.form.get('q2')

    if q1 == "Language":
        score += 1

    if q2 == "#":
        score += 1

    return render_template('result.html', score=score)
@app.route('/resume', methods=['GET', 'POST'])
def resume():

    if request.method == 'POST':

        file = request.files['resume']

        if file:
            file.save(os.path.join('uploads', file.filename))
            return f"Resume Uploaded Successfully: {file.filename}"

    return render_template('resume_analyzer.html')

if __name__ == '__main__':
    app.run(debug=True)