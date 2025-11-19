from flask import Flask, render_template, request, redirect, session


# Product Model
class Product(db.Model):
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(100))
price = db.Column(db.String(50))
description = db.Column(db.String(200))
seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))


@app.before_first_request
def create_tables():
db.create_all()


@app.route('/')
def index():
products = Product.query.all()
return render_template("index.html", products=products)


@app.route('/register', methods=['GET', 'POST'])
def register():
if request.method == 'POST':
username = request.form['username']
password = generate_password_hash(request.form['password'])
user = User(username=username, password=password)
db.session.add(user)
db.session.commit()
return redirect('/login')
return render_template('register.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
if request.method == 'POST':
username = request.form['username']
password = request.form['password']
user = User.query.filter_by(username=username).first()
if user and check_password_hash(user.password, password):
session['user_id'] = user.id
return redirect('/dashboard')
return render_template('login.html')


@app.route('/dashboard')
def dashboard():
if 'user_id' not in session:
return redirect('/login')
products = Product.query.filter_by(seller_id=session['user_id']).all()
return render_template('dashboard.html', products=products)


@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
if 'user_id' not in session:
return redirect('/login')


if request.method == 'POST':
name = request.form['name']
price = request.form['price']
description = request.form['description']
new_product = Product(name=name, price=price, description=description, seller_id=session['user_id'])
db.session.add(new_product)
db.session.commit()
return redirect('/dashboard')


return render_template('add_product.html')


if __name__ == '__main__':
app.run(debug=True)