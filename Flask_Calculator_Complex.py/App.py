from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        try:
            total = float(request.form['total'])
            obtained = float(request.form['obtained'])
            if total > 0:
                result = (obtained / total) * 100
            else:
                result = 'Total must be greater than zero'
        except ValueError:
            result = 'Please enter valid numbers'
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)
