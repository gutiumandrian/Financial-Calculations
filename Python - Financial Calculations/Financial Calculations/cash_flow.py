#Module 1: Cash Flow Calculations
#This module calculates net cash flows over a given period.

import pandas as pd

def calculate_cash_flow(inflows, outflows):
    """
    Calculate net cash flow for inflows and outflows.
    """
    if len(inflows) != len(outflows):
        raise ValueError("Inflows and outflows must have the same length.")
    data = {
        "Inflows": inflows,
        "Outflows": outflows,
        "Net Cash Flow": [inflow - outflow for inflow, outflow in zip(inflows, outflows)]
    }
    return pd.DataFrame(data)

