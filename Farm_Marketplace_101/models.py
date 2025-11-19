from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


db = SQLAlchemy()


class User(db.Model):
id = db.Column(db.Integer, primary_key=True)
username = db.Column(db.String(80), unique=True, nullable=False)
email = db.Column(db.String(120), unique=True, nullable=False)
password_hash = db.Column(db.String(200), nullable=False)
is_seller = db.Column(db.Boolean, default=False)
products = db.relationship('Product', backref='seller', lazy=True)
ratings = db.relationship('Rating', backref='user', lazy=True)


class Product(db.Model):
id = db.Column(db.Integer, primary_key=True)
name = db.Column(db.String(120), nullable=False)
description = db.Column(db.Text)
price = db.Column(db.Float, nullable=False)
category = db.Column(db.String(80))
image_filename = db.Column(db.String(200))
created_at = db.Column(db.DateTime, default=datetime.utcnow)
seller_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
ratings = db.relationship('Rating', backref='product', lazy=True)


class Rating(db.Model):
id = db.Column(db.Integer, primary_key=True)
user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
product_id = db.Column(db.Integer, db.ForeignKey('product.id'), nullable=False)
score = db.Column(db.Integer, nullable=False) # 1..5
review = db.Column(db.Text)
created_at = db.Column(db.DateTime, default=datetime.utcnow)