#Module 2: Present and Future Value Calculations
#Calculates present and future values.
def present_value(future_value, rate, periods):
    """
    Calculate present value of a future amount.
    """
    return future_value / (1 + rate) ** periods

def future_value(present_value, rate, periods):
    """
    Calculate future value of a present amount.
    """
    return present_value * (1 + rate) ** periods

