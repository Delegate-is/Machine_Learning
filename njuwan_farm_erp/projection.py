from database import db
from models import MilkProduction, Transaction, Cow, Crop
from sqlalchemy import func

def three_year_projection():
    # --- Current baseline values ---
    current_milk = db.session.query(func.sum(MilkProduction.litres)).scalar() or 0
    current_income = db.session.query(func.sum(Transaction.amount)).filter_by(type="Income").scalar() or 0
    current_expense = db.session.query(func.sum(Transaction.amount)).filter_by(type="Expense").scalar() or 0
    current_cows = db.session.query(func.count(Cow.id)).scalar() or 0
    current_acreage = db.session.query(func.sum(Crop.acreage)).scalar() or 0

    # --- Growth assumptions ---
    milk_growth = 0.15
    cost_inflation = 0.06
    herd_increase = 10
    acreage_increase = 10

    projections = []

    milk = current_milk
    income = current_income
    expense = current_expense
    cows = current_cows
    acreage = current_acreage

    for year in range(1, 4):
        milk *= (1 + milk_growth)
        income *= (1 + milk_growth)
        expense *= (1 + cost_inflation)
        cows += herd_increase
        acreage += acreage_increase

        profit = income - expense

        projections.append({
            "year": f"Year {year}",
            "milk": round(milk, 2),
            "income": round(income, 2),
            "expense": round(expense, 2),
            "profit": round(profit, 2),
            "cows": cows,
            "acreage": acreage
        })

    return projections