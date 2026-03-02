from database import db
from models import YoghurtProduction
from sqlalchemy import func

def yoghurt_profit_analysis():

    records = YoghurtProduction.query.all()

    total_milk_used = 0
    total_cups = 0
    total_revenue = 0
    total_cost = 0

    for record in records:
        total_milk_used += record.milk_used_litres
        total_cups += record.cups_produced
        total_revenue += record.cups_produced * record.selling_price_per_cup
        total_cost += record.processing_cost + record.packaging_cost

    profit = total_revenue - total_cost
    margin = (profit / total_revenue * 100) if total_revenue > 0 else 0

    return {
        "milk_used": total_milk_used,
        "cups": total_cups,
        "revenue": round(total_revenue, 2),
        "cost": round(total_cost, 2),
        "profit": round(profit, 2),
        "margin": round(margin, 2)
    }