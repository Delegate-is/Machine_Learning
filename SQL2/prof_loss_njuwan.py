import pandas as pd
from sqlalchemy import create_engine
from datetime import datetime

def generate_monthly_report(month, year):
    # 1. Connect to your local 'avatar' database
    engine = create_engine("mysql+pymysql://root:@localhost/avatar")
    
    # 2. Query to get Income and Expenses for the specific month
    query = f"""
    SELECT transaction_type, category, amount 
    FROM farm_finances 
    WHERE MONTH(transaction_date) = {month} AND YEAR(transaction_date) = {year}
    """
    
    try:
        df = pd.read_sql(query, engine)
        
        if df.empty:
            return "No data found for the selected period."

        # 3. Calculate Totals
        total_income = df[df['transaction_type'] == 'Income']['amount'].sum()
        total_expense = df[df['transaction_type'] == 'Expense']['amount'].sum()
        net_profit = total_income - total_expense
        profit_margin = (net_profit / total_income * 100) if total_income > 0 else 0

        # 4. Display the Report
        print(f"--- Njuwan Farm P&L Report: {month}/{year} ---")
        print(f"Total Revenue:  KES {total_income:,.2f}")
        print(f"Total Expenses: KES {total_expense:,.2f}")
        print(f"-------------------------------------------")
        print(f"Net Profit:     KES {net_profit:,.2f}")
        print(f"Profit Margin:  {profit_margin:.1f}%")
        
        if net_profit > 0:
            print("Status: Target Growth on Track ✅")
        else:
            print("Status: Action Required (Loss) ⚠️")

    except Exception as e:
        print(f"Error generating report: {e}")

# Example: Generate report for February 2026
generate_monthly_report(2, 2026)