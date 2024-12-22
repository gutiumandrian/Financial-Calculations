#Module 3: Financial Metrics 
def net_present_value(rate, cash_flows):
    return sum(cf / (1 + rate) ** i for i, cf in enumerate(cash_flows))


def internal_rate_of_return(cash_flows, max_iterations=1000, tolerance=1e-6):
    irr = 0.1  # Initial guess
    for _ in range(max_iterations):
        npv = sum(cf / (1 + irr) ** i for i, cf in enumerate(cash_flows))
        d_npv = sum(-i * cf / (1 + irr) ** (i + 1) for i, cf in enumerate(cash_flows))
        if d_npv == 0:
            break
        irr_new = irr - npv / d_npv
        if abs(irr_new - irr) < tolerance:
            return irr_new
        irr = irr_new
    raise ValueError("IRR calculation did not converge")

