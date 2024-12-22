# Module 3: Financial Metrics

cash_flows = [-1000, 300, 420, 680, 850]
npv = net_present_value(rate=0.1, cash_flows=cash_flows)
irr = internal_rate_of_return(cash_flows)
print(f"\nNet Present Value at 10%: ${npv:.2f}")
print(f"Internal Rate of Return: {irr:.2%}")