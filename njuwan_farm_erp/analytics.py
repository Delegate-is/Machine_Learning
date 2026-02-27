from models import MilkProduction, Transaction, Cow
from database import db
from sqlalchemy import extract, func
from models import Crop, CropCost, CropYield

def monthly_milk_data():
    data = db.session.query(
        extract('month', MilkProduction.date).label('month'),
        func.sum(MilkProduction.litres)
    ).group_by('month').all()

    months = [int(row[0]) for row in data]
    totals = [float(row[1]) for row in data]

    return months, totals


def revenue_vs_expense():
    income = db.session.query(func.sum(Transaction.amount)).filter_by(type="Income").scalar() or 0
    expense = db.session.query(func.sum(Transaction.amount)).filter_by(type="Expense").scalar() or 0
    return income, expense


def cow_profitability():
    cows = db.session.query(Cow).all()
    results = []

    for cow in cows:
        milk_total = db.session.query(func.sum(MilkProduction.litres)).filter_by(cow_id=cow.id).scalar() or 0
        results.append({
            "cow": cow.tag_number,
            "milk": milk_total
        })

    results.sort(key=lambda x: x["milk"], reverse=True)
    return results

def crop_roi_analysis():
    crops = Crop.query.all()
    results = []

    for crop in crops:
        total_cost = db.session.query(func.sum(CropCost.amount)).filter_by(crop_id=crop.id).scalar() or 0
        total_revenue = db.session.query(func.sum(CropYield.revenue)).filter_by(crop_id=crop.id).scalar() or 0

        roi = ((total_revenue - total_cost) / total_cost * 100) if total_cost > 0 else 0

        results.append({
            "name": crop.name,
            "cost": total_cost,
            "revenue": total_revenue,
            "roi": round(roi, 2)
        })

    return results