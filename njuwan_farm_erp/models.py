from flask_sqlalchemy import SQLAlchemy
from database import db
from datetime import datetime

# ======================
# DAIRY MODULE
# ======================

class Cow(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(50), unique=True)
    breed = db.Column(db.String(100))
    birth_date = db.Column(db.Date)
    status = db.Column(db.String(50))  # lactating, dry, sold


class MilkProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cow.id'))
    date = db.Column(db.Date, default=datetime.utcnow)
    litres = db.Column(db.Float)


class FeedUsage(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer)
    feed_type = db.Column(db.String(100))
    quantity_kg = db.Column(db.Float)
    cost = db.Column(db.Float)
    date = db.Column(db.Date, default=datetime.utcnow)


# ======================
# CROPS MODULE
# ======================

class Crop(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    acreage = db.Column(db.Float)
    season = db.Column(db.String(50))


class CropCost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))
    amount = db.Column(db.Float)
    description = db.Column(db.String(200))


class CropYield(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    crop_id = db.Column(db.Integer, db.ForeignKey('crop.id'))
    quantity = db.Column


# ======================
# INVENTORY MODULE
# ======================

class InventoryItem(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    category = db.Column(db.String(50))
    quantity = db.Column(db.Float)
    unit = db.Column(db.String(20))
    reorder_level = db.Column(db.Float)
    cost_per_unit = db.Column(db.Float)


# ======================
# FINANCE MODULE
# ======================

class Transaction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, default=datetime.utcnow)
    category = db.Column(db.String(100))
    amount = db.Column(db.Float)
    type = db.Column(db.String(10))  # income / expense