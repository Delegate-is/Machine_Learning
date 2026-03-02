from projection import three_year_projection

def farm_valuation():

    projections = three_year_projection()

    discount_rate = 0.15  # 15% investor expected return
    terminal_growth = 0.05
    ebitda_multiple = 6

    discounted_cashflows = 0

    for i, year in enumerate(projections):
        profit = year["profit"]
        discounted = profit / ((1 + discount_rate) ** (i + 1))
        discounted_cashflows += discounted

    # Terminal Value (Gordon Growth Model)
    final_year_profit = projections[-1]["profit"]
    terminal_value = (final_year_profit * (1 + terminal_growth)) / (discount_rate - terminal_growth)

    discounted_terminal = terminal_value / ((1 + discount_rate) ** 3)

    dcf_value = discounted_cashflows + discounted_terminal

    # EBITDA Multiple Method
    ebitda_value = final_year_profit * ebitda_multiple

    return {
        "dcf_value": round(dcf_value, 2),
        "ebitda_value": round(ebitda_value, 2),
        "terminal_value": round(terminal_value, 2)
    }