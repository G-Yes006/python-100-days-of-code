# Define the SIP parameters
monthly_investment = 15000  # in INR
investment_period_months = 10 * 12  # 10 years
annual_return_rate_10 = 0.10  # 10% annual return
annual_return_rate_15 = 0.15  # 15% annual return
ltcg_tax_rate = 0.10  # 10% LTCG tax

# SIP future value formula


def sip_future_value(monthly_investment, annual_return_rate, investment_period_months):
    monthly_rate = annual_return_rate / 12
    future_value = monthly_investment * \
        (((1 + monthly_rate) ** investment_period_months - 1) /
         monthly_rate) * (1 + monthly_rate)
    return round(future_value)


# Calculate future values
future_value_10 = sip_future_value(
    monthly_investment, annual_return_rate_10, investment_period_months)
future_value_15 = sip_future_value(
    monthly_investment, annual_return_rate_15, investment_period_months)

# Calculate total investment
total_investment = monthly_investment * investment_period_months

# Calculate capital gains
capital_gains_10 = future_value_10 - total_investment
capital_gains_15 = future_value_15 - total_investment

# Calculate LTCG tax
ltcg_tax_10 = max(0, capital_gains_10 - 100000) * ltcg_tax_rate
ltcg_tax_15 = max(0, capital_gains_15 - 100000) * ltcg_tax_rate

# Calculate post-tax future values
post_tax_value_10 = round(future_value_10 - ltcg_tax_10)
post_tax_value_15 = round(future_value_15 - ltcg_tax_15)

print(future_value_10, post_tax_value_10, future_value_15, post_tax_value_15)
