from flask import Flask, render_template, request, redirect
from config import Config
from database import db
from datetime import datetime
from version import increment_version
from project_state import load_state
from models import MilkProduction, Transaction, Cow
from analytics import monthly_milk_data, revenue_vs_expense, cow_profitability, crop_roi_analysis

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
            tag_number=request.form["tag"],
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

if __name__ == "__main__":
    app.run(debug=True)