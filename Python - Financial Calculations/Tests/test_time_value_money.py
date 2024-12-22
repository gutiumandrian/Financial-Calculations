# Module 2: Present and Future Value

from financial_calculations.time_value_money import present_value, future_value

pv = present_value(5000, rate=0.05, periods=10)
fv = future_value(3000, rate=0.05, periods=10)
print(f"Present Value: ${pv:.2f}")
print(f"Future Value: ${fv:.2f}")
