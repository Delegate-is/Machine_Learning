from models import MilkProduction, Transaction, Cow
from database import db
from sqlalchemy import extract, func
from models import Crop #CropCost, CropYield, FeedConsumption, FeedType
from models import Feed, MilkProduction, Cow 

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

"""def crop_roi_analysis():
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
"""

def feed_efficiency_model():
    from models import Feed, MilkProduction
    from sqlalchemy import func

    # Calculate total milk once
    total_milk = db.session.query(func.sum(MilkProduction.litres)).scalar() or 0
    
    # Calculate total feed cost in one query
    all_feed = Feed.query.all()
    total_feed_cost = sum(record.total_cost for record in all_feed)

    cost_per_litre_feed = (total_feed_cost / total_milk) if total_milk > 0 else 0

    # Sensitivity: 5% feed cost reduction logic
    reduced_cost = total_feed_cost * 0.95
    improved_cost_per_litre = (reduced_cost / total_milk) if total_milk > 0 else 0

    return {
        "total_feed_cost": round(total_feed_cost, 2),
        "feed_cost_per_litre": round(cost_per_litre_feed, 2),
        "optimized_cost_per_litre": round(improved_cost_per_litre, 2)
    }

def cow_feed_efficiency():
    # Update these imports to match your actual model names

    cows = Cow.query.all()
    results = []

    for cow in cows:
        # Filter by cow.id to match the Foreign Key relationship
        milk_total = db.session.query(func.sum(MilkProduction.litres)).filter_by(cow_id=cow.id).scalar() or 0
        
        # Use 'Feed' instead of 'FeedConsumption'
        feed_records = Feed.query.filter_by(cow_id=cow.id).all()
        total_feed = sum(record.qty for record in feed_records) # Use 'qty' as per your Feed model

        efficiency = (milk_total / total_feed) if total_feed > 0 else 0

        results.append({
            "cow": cow.tag_number,
            "name": cow.name,
            "milk": round(milk_total, 2),
            "feed_kg": round(total_feed, 2),
            "efficiency": round(efficiency, 2),
            "status": cow.status
        })

    results.sort(key=lambda x: x["efficiency"], reverse=True)
    return results

def get_monthly_report():
    # This query sums up litres grouped by Year and Month
    report = db.session.query(
        extract('year', MilkProduction.date).label('year'),
        extract('month', MilkProduction.date).label('month'),
        func.sum(MilkProduction.litres).label('total_litres'),
        func.avg(MilkProduction.temperature).label('avg_temp')
    ).group_by('year', 'month').order_by('year', 'month').all()
    
    return report