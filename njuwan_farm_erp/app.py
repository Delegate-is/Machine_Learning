# pip install -r requirements.txt
from flask import Flask, render_template, request, redirect
from config import Config
from database import db
from datetime import datetime
from version import increment_version
from project_state import load_state
from models import MilkProduction, Transaction, Cow, Crop, Feed
from analytics import monthly_milk_data, revenue_vs_expense, cow_profitability, crop_roi_analysis
from projection import three_year_projection
from analytics import feed_efficiency_model
from analytics import cow_feed_efficiency
from yoghurt_engine import yoghurt_profit_analysis
from valuation_engine import farm_valuation
from flask import jsonify

app = Flask(__name__)
app.config.from_object(Config)

# 3. Initialize the app with the db instance
db.init_app(app)

with app.app_context():
    # This creates the tables based on tag_number and other fields in models.py
    db.create_all()

current_version = increment_version()
print(f"Njuwan Farm ERP Version: {current_version}")

with app.app_context():
    db.create_all()

# ======================
# DASHBOARD
# ======================

@app.route("/")
def dashboard():
    total_milk = db.session.query(db.func.sum(MilkProduction.litres)).scalar() or 0
    total_income = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Income").scalar() or 0
    total_expense = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Expense").scalar() or 0

    cost_per_litre = round(total_expense / total_milk, 2) if total_milk > 0 else 0
    net_profit = total_income - total_expense

    return render_template(
        "dashboard.html",
        total_milk=total_milk,
        cost_per_litre=cost_per_litre,
        net_profit=net_profit
    )

# ======================
# ADD COW
# ======================

@app.route("/add_cow", methods=["GET", "POST"])
def add_cow():
    if request.method == "POST":
        cow = Cow(
            tag_number=request.form["tag_number"],
            breed=request.form["breed"],
            birth_date=datetime.strptime(request.form["birth"], "%Y-%m-%d"),
            status=request.form["status"]
        )
        db.session.add(cow)
        db.session.commit()
        return redirect("/")
    return render_template("add_cow.html")


# ======================
# ADD MILK RECORD
# ======================

@app.route("/add_milk", methods=["GET", "POST"])
def add_milk():
    if request.method == "POST":
        milk = MilkProduction(
            cow_id=request.form["cow_id"],
            litres=float(request.form["litres"]),
            date=datetime.now()
        )
        db.session.add(milk)
        db.session.commit()
        return redirect("/")
    cows = Cow.query.all()
    return render_template("add_milk.html", cows=cows)


# ======================
# ADD TRANSACTION
# ======================

@app.route("/add_transaction", methods=["GET", "POST"])
def add_transaction():
    if request.method == "POST":
        t = Transaction(
            category=request.form["category"],
            amount=float(request.form["amount"]),
            type=request.form["type"]
        )
        db.session.add(t)
        db.session.commit()
        return redirect("/")
    return render_template("add_transaction.html")

@app.route("/progress")
def progress():
    state = load_state()
    return render_template("progress.html", state=state)

@app.route("/analytics")
def analytics_dashboard():
    months, milk_totals = monthly_milk_data()
    income, expense = revenue_vs_expense()
    cow_rank = cow_profitability()
    crop_data = crop_roi_analysis()

    return render_template(
        "analytics.html",
        months=months,
        milk_totals=milk_totals,
        income=income,
        expense=expense,
        cow_rank=cow_rank,
        crop_data=crop_data,
    )

@app.route("/projection")
def projection_dashboard():
    data = three_year_projection()
    return render_template("projection.html", data=data)

@app.route("/feed-efficiency")
def feed_efficiency():
    data = feed_efficiency_model()
    return render_template("feed_efficiency.html", data=data)

@app.route("/cow_efficiency")
def cow_efficiency():
    data = cow_feed_efficiency()
    return render_template("cow_efficiency.html", data=data)

@app.route("/yoghurt")
def yoghurt_dashboard():
    data = yoghurt_profit_analysis()
    return render_template("yoghurt.html", data=data)

@app.route("/valuation")
def valuation_dashboard():
    data = farm_valuation()
    return render_template("valuation.html", data=data)

@app.route('/add_crop', methods=['GET', 'POST'])
def add_crop():
    if request.method == 'POST':
        # Your logic to save the crop to the database
        crop = Crop(
            id=request.form["tag"],
            name=request.form["crop"],
            acreage=float(request.form["acre"]),
            planting_date=datetime.strptime(request.form["planting_date"], "%Y-%m-%d")
        )
        db.session.add(crop)
        db.session.commit()
        return redirect("/")
    return render_template('add_crop.html')

@app.route('/add_feed', methods=['GET', 'POST'])
def add_feed_entry():  # Unique name to avoid AssertionError
    if request.method == 'POST':
        # Data cleaning and validation logic
        tag = request.form.get('tag_number')
        feed_type = request.form.get('feed_type')
        quantity = float(request.form.get('quantity'))
        cost = float(request.form.get('cost'))
        
        # Save to database (assumes you have a Feed model)
        new_feed = Feed(tag_number=tag, f_type=feed_type, qty=quantity, cost=cost)
        db.session.add(new_feed)
        db.session.commit()
        return redirect("/")  # Redirect to dashboard or feed list after adding        
    return render_template('add_feed.html')

@app.route("/api/kpis")
def api_kpis():
    total_milk = db.session.query(db.func.sum(MilkProduction.litres)).scalar() or 0
    total_income = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Income").scalar() or 0
    total_expense = db.session.query(db.func.sum(Transaction.amount)).filter_by(type="Expense").scalar() or 0
    
    return jsonify({
        "milk": total_milk,
        "income": total_income,
        "expense": total_expense
    })

if __name__ == "__main__":
    app.run(debug=True)