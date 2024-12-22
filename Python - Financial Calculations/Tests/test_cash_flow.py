# Module 1: Cash Flow Calculations

from financial_calculations.cash_flow import calculate_cash_flow

inflows = [1000, 1500, 2000, 2500]
outflows = [500, 700, 800, 1000]
cash_flow_df = calculate_cash_flow(inflows, outflows)
print(cash_flow_df)
