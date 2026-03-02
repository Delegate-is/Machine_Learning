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

def feed_efficiency_model():
    from models import FeedConsumption, FeedType, MilkProduction, Cow

    total_feed_cost = 0
    total_milk = db.session.query(func.sum(MilkProduction.litres)).scalar() or 0

    consumptions = db.session.query(FeedConsumption).all()

    for record in consumptions:
        feed = db.session.get(FeedType, record.feed_id)
        if feed:
            total_feed_cost += record.quantity_kg * feed.cost_per_kg

    cost_per_litre_feed = (total_feed_cost / total_milk) if total_milk > 0 else 0

    # Sensitivity: 5% feed cost reduction
    reduced_cost = total_feed_cost * 0.95
    improved_cost_per_litre = (reduced_cost / total_milk) if total_milk > 0 else 0

    return {
        "total_feed_cost": round(total_feed_cost, 2),
        "feed_cost_per_litre": round(cost_per_litre_feed, 2),
        "optimized_cost_per_litre": round(improved_cost_per_litre, 2)
    }
    
def cow_feed_efficiency():
    from models import FeedConsumption, MilkProduction, Cow, FeedType

    cows = Cow.query.all()
    results = []

    for cow in cows:
        milk_total = db.session.query(func.sum(MilkProduction.litres)).filter_by(cow_id=cow.id).scalar() or 0
        
        feed_records = db.session.query(FeedConsumption).filter_by(cow_id=cow.id).all()
        total_feed = 0

        for record in feed_records:
            feed = db.session.get(FeedType, record.feed_id)
            if feed:
                total_feed += record.quantity_kg

        efficiency = (milk_total / total_feed) if total_feed > 0 else 0

        results.append({
            "cow": cow.tag,
            "milk": milk_total,
            "feed_kg": total_feed,
            "efficiency": round(efficiency, 2)
        })

    results.sort(key=lambda x: x["efficiency"], reverse=True)
    return results