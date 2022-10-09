def cook_pasta(cook_time: int, water_temp: int, pasta_type: str) -> str:
    """Cook pasta.
    Args:
        cook_time: The time to cook the pasta.
        water_temp: The temperature of the water.
        pasta_type: The type of pasta to cook.
    Returns:
        The cooked pasta.
    """
    return f"Cooking {pasta_type} for {cook_time} minutes at {water_temp} degrees."
