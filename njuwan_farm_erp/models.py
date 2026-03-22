from flask_sqlalchemy import SQLAlchemy
from database import db
from datetime import datetime
from datetime import date


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
    farm_id = db.Column(db.Integer, db.ForeignKey("farms.id"))
    # ... other fields ...
    # Advanced Tracking Fields
    weight_kg = db.Column(db.Float) # Useful for health monitoring
    # 1. RENAME the actual column in the database
    # We use "status" as the DB name, but _status as the Python variable
    _status = db.Column("status", db.String(50), default="Lactating")
    
    @property
    def age_in_years(self):
        from datetime import date
        if self.date_of_birth:
            return (date.today() - self.date_of_birth).days // 365
        return "Unknown"

    @property
    def status(self):
        if self.name and "Calf" in self.name:
            return "Young"

        latest = Breeding.query.filter_by(cow_id=self.id).order_by(Breeding.id.desc()).first()
    
        if latest and latest.expected_calving:
            from datetime import datetime
            # FIX: Convert now to a date object to match expected_calving
            today = datetime.now().date()
            days_to_calving = (latest.expected_calving - today).days
        
            if 0 < days_to_calving <= 60:
                return "Dry"
            elif days_to_calving > 60:
                return "Pregnant"

        # Use _status to avoid the recursion loop we saw earlier
        return self._status or "Lactating"

    @status.setter
    def status(self, value):
        self._status = value
    
    # Define the relationship ONLY ONCE. 
    # backref="cow" automatically creates a 'cow' attribute on the Feed object.
    feed_records = db.relationship("Feed", backref="cow", lazy=True)
    milk_records = db.relationship("MilkProduction", backref="cow", lazy='dynamic')
    health_records = db.relationship('HealthRecord', backref='cow', lazy=True)
    vaccinations = db.relationship('Vaccination', backref='cow', lazy=True)
    breeding_records = db.relationship('Breeding', backref='cow', lazy=True)
    
class HealthRecord(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'))
    disease = db.Column(db.String(100))
    treatment = db.Column(db.String(200))
    vet_name = db.Column(db.String(100))
    cost = db.Column(db.Float)
    date = db.Column(db.Date, default=datetime.utcnow) # Automatically stamps entry date
    status = db.Column(db.String(20), default="Under Treatment")
    clearance_date = db.Column(db.DateTime, nullable=True)
    
class Vaccination(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'))
    vaccine = db.Column(db.String(100))
    due_date = db.Column(db.Date)
    administered_by = db.Column(db.String(100))
    next_due_date = db.Column(db.Date)
    status = db.Column(db.String(20), default="Pending") # Matches your HTML badges

class Breeding(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cow_id = db.Column(db.Integer, db.ForeignKey('cows.id'))
    insemination_date = db.Column(db.Date)
    bull = db.Column(db.String(50))
    pregnancy_status = db.Column(db.String(20), default="Unknown")
    expected_calving = db.Column(db.Date) # Calculated via your app.py logic
    
    @property
    def days_remaining(self):
        if self.expected_calving:
            delta = self.expected_calving - date.today()
            return delta.days if delta.days > 0 else 0
        return None

# ===============================
# MILK PRODUCTION
# ===============================

class MilkProduction(db.Model):
    __tablename__ = "milk_production"

    id = db.Column(db.Integer, primary_key=True)

    cow_id = db.Column(db.Integer, db.ForeignKey("cows.id"))

    litres = db.Column(db.Float)
    
    # Advanced Production Fields
    session = db.Column(db.String(10)) # AM, PM, or Noon
    temperature = db.Column(db.Float) # Milk temperature for quality control
    date = db.Column(db.DateTime, default=datetime.utcnow)
    
    def is_quality_standard(self):
        # Example: Normal fresh milk temp is usually 35-38°C at milking
        return 34.0 <= self.temperature <= 39.0

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
    
class CalfHealth(db.Model):
    __tablename__ = "calf_health"
    id = db.Column(db.Integer, primary_key=True)
    calf_id = db.Column(db.Integer, db.ForeignKey('cows.id'), nullable=False)
    colostrum_litres = db.Column(db.Float, default=0.0)
    colostrum_time = db.Column(db.DateTime) # Critical within 2 hours
    navel_dipped = db.Column(db.Boolean, default=False)
    vitamin_booster = db.Column(db.Boolean, default=False)
    check_date = db.Column(db.DateTime, default=datetime.utcnow)
    
class Inventory(db.Model):
    __tablename__ = "inventory"
    id = db.Column(db.Integer, primary_key=True)
    item_name = db.Column(db.String(100), unique=True, nullable=False)
    quantity = db.Column(db.Float, default=0.0)
    unit = db.Column(db.String(20)) # e.g., 'Litres', 'Kg'
    min_threshold = db.Column(db.Float, default=5.0) # Alert if below this
    last_updated = db.Column(db.DateTime, default=datetime.utcnow)