from flask_sqlalchemy import SQLAlchemy
from database import db
from datetime import datetime


# ===============================
# USERS
# ===============================

"""class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    role = db.Column(db.String(20))  # Admin / Worker / Investor
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    farm_id = db.Column(db.Integer, db.ForeignKey("farms.id"))

    def __repr__(self):
        return f"<User {self.username}>"
"""

# ===============================
# FARMS (Multi Farm Support)
# ===============================

class Farm(db.Model):
    __tablename__ = "farms"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(150))
    acreage = db.Column(db.Float)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    cows = db.relationship("Cow", backref="farm")
    crops = db.relationship("Crop", backref="farm")



# ===============================
# COWS
# ===============================

class Cow(db.Model):
    __tablename__ = "cows"
    
    id = db.Column(db.Integer, primary_key=True)
    tag_number = db.Column(db.String(50), unique=True)
    name = db.Column(db.String(100))  # New Name Column
    breed = db.Column(db.String(50))
    birth_date = db.Column(db.Date)
    age = db.Column(db.Integer)
    status = db.Column(db.String(50))  # Lactating / Dry / Sold
    farm_id = db.Column(db.Integer, db.ForeignKey("farms.id"))
    # ... other fields ...

    # Define the relationship ONLY ONCE. 
    # backref="cow" automatically creates a 'cow' attribute on the Feed object.
    feed_records = db.relationship("Feed", backref="cow", lazy=True)
    milk_records = db.relationship("MilkProduction", backref="cow", lazy=True)




# ===============================
# MILK PRODUCTION
# ===============================

class MilkProduction(db.Model):
    __tablename__ = "milk_production"

    id = db.Column(db.Integer, primary_key=True)

    cow_id = db.Column(db.Integer, db.ForeignKey("cows.id"))

    litres = db.Column(db.Float)
    date = db.Column(db.DateTime, default=datetime.utcnow)



# ===============================
# FEED RECORDS
# ===============================

class Feed(db.Model):
    __tablename__ = "feed_records"

    id = db.Column(db.Integer, primary_key=True)
    
    # Use only cow_id as the primary link. 
    # Remove the redundant tag_number foreign key to stop the error.
    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'), nullable=False)
    
    f_type = db.Column(db.String(100))
    qty = db.Column(db.Float)
    cost = db.Column(db.Float)
    # Add a temporary default value (like 0.0) so the migration can finish
    cost_per_kg = db.Column(db.Float, nullable=False, default=0.0) #Store cost per kg for easier calculations later
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    @property
    def total_cost(self):
        return self.qty * self.cost_per_kg
    
# ===============================
# CROPS
# ===============================

class Crop(db.Model):
    __tablename__ = "crops"

    id = db.Column(db.Integer, primary_key=True)

    name = db.Column(db.String(100))
    acreage = db.Column(db.Float)

    planting_date = db.Column(db.Date)
    harvest_date = db.Column(db.Date)

    cost = db.Column(db.Float)
    revenue = db.Column(db.Float)

    farm_id = db.Column(db.Integer, db.ForeignKey("farms.id"))



# ===============================
# FINANCIAL TRANSACTIONS
# ===============================

class Transaction(db.Model):
    __tablename__ = "transactions"

    id = db.Column(db.Integer, primary_key=True)

    category = db.Column(db.String(100))
    amount = db.Column(db.Float)

    type = db.Column(db.String(20))  # Income / Expense

    date = db.Column(db.DateTime, default=datetime.utcnow)



# ===============================
# YOGHURT PRODUCTION
# ===============================

class YoghurtProduction(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    milk_used_litres = db.Column(db.Float)
    cups_produced = db.Column(db.Integer)
    selling_price_per_cup = db.Column(db.Float)
    processing_cost = db.Column(db.Float)
    packaging_cost = db.Column(db.Float)
    production_date = db.Column(db.DateTime, default=datetime.utcnow)
    
# ===============================
# FARM VALUATION HISTORY
# ===============================

class FarmValuation(db.Model):
    __tablename__ = "farm_valuations"

    id = db.Column(db.Integer, primary_key=True)

    valuation = db.Column(db.Float)
    projected_profit = db.Column(db.Float)

    valuation_date = db.Column(db.DateTime, default=datetime.utcnow)