from flask import Flask, render_template, request, redirect, session
from flask_sqlalchemy import SQLAlchemy
import os

app = Flask(__name__)
app.secret_key = "supersecret"

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///farm.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['UPLOAD_FOLDER'] = "static/uploads"

db = SQLAlchemy(app)

class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    price = db.Column(db.String(50))
    description = db.Column(db.String(200))
    image_filename = db.Column(db.String(200))
    seller_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(80), unique=True)
    password = db.Column(db.String(200))
    products = db.relationship('Product', backref='seller', lazy=True)


@app.before_request
def setup():
    db.create_all()


@app.route('/')
def index():
    products = Product.query.all()
    return render_template('index.html', products=products)


@app.route('/register', methods=["GET", "POST"])
def register():
    if request.method == "POST":
        user = User(
            username=request.form["username"],
            email=request.form["email"],
            password=request.form["password"]
        )
        db.session.add(user)
        db.session.commit()
        return redirect("/login")
    return render_template("register.html")


@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = User.query.filter_by(username=request.form["username"]).first()
        if user and user.password == request.form["password"]:
            session["user_id"] = user.id
            return redirect("/dashboard")
    return render_template("login.html")


@app.route('/dashboard')
def dashboard():
    if "user_id" not in session:
        return redirect("/login")
    products = Product.query.filter_by(seller_id=session["user_id"]).all()
    return render_template("dashboard.html", products=products)


@app.route('/add_product', methods=["GET", "POST"])
def add_product():
    if "user_id" not in session:
        return redirect("/login")

    if request.method == "POST":

        # Handle image upload
        image_file = request.files.get("image")
        filename = None
        if image_file:
            filename = image_file.filename
            path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
            image_file.save(path)

        product = Product(
            name=request.form["name"],
            price=request.form["price"],
            description=request.form["description"],
            seller_id=session["user_id"],
            image_filename=filename
        )

        db.session.add(product)
        db.session.commit()
        return redirect("/dashboard")

    return render_template("add_product.html")


if __name__ == "__main__":
    app.run(debug=True)
# To run:
# python -m venv .venv
# .\.venv\Scripts\activate
# python -m pip install Flask
# pip install -r requirements.txt
# python app.py
