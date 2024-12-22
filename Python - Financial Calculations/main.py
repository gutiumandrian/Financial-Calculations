# Example
from financial_calculations.cash_flow import calculate_cash_flow
from financial_calculations.time_value_money import present_value, future_value
from financial_calculations.metrics import net_present_value, internal_rate_of_return

if __name__ == "__main__":
    # Example 1: Cash Flow Calculation
    inflows = [1000, 1500, 2000, 2500]
    outflows = [500, 700, 800, 1000]
    cash_flow_df = calculate_cash_flow(inflows, outflows)
    print("Cash Flow Table:")
    print(cash_flow_df)

    # Example 2: Present and Future Value
    pv = present_value(5000, rate=0.05, periods=10)
    fv = future_value(3000, rate=0.05, periods=10)
    print(f"\nPresent Value of $5000 in 10 years at 5%: ${pv:.2f}")
    print(f"Future Value of $3000 in 10 years at 5%: ${fv:.2f}")

    # Example 3: Financial Metrics
    cash_flows = [-1000, 300, 420, 680, 850]
    npv = net_present_value(rate=0.1, cash_flows=cash_flows)
    irr = internal_rate_of_return(cash_flows)
    print(f"\nNet Present Value at 10%: ${npv:.2f}")
    print(f"Internal Rate of Return: {irr:.2%}")

