# Error Handling
def validate_numeric(value, name="value"):
    """
    Validate that a value is numeric.
    """
    if not isinstance(value, (int, float)):
        raise ValueError(f"{name} must be numeric.")

