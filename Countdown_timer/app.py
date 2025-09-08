from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/countdown', methods=['POST'])
def countdown():
    start = int(request.form['start'])
    end = int(request.form['end'])
    return render_template('countdown.html', start=start, end=end)

if __name__ == '__main__':
    app.run(debug=True)
