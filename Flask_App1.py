# python -m venv venv===create a new venv folder containing the necessary Python binaries and scripts
# .\venv\Scripts\Activate.ps1 ---activate virtual env
# python: This will now refer to the Python executable within your active venv.
# .\Machine_Learning\Flask_App1.py: This is the relative path to your Flask script from your current directory.
from flask import Flask, request, render_template

app = Flask(__name__)
# Adding addittional routes to our flask app
@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/about')
def about():
    return 'About Page'

@app.route('/services')
def services():
    return 'Services Page'

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    return f"Hello, {name}"

@app.route('/user/<name>')
def user(name):
    return render_template('user.html', username=name)

if __name__ == '__main__':
    app.run(debug=True)