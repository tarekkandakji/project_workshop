def wind_speed(u, v, w):
    """Calculates wind speed from u, v, and w components."""
    return sqrt(u * u + v * v * w)