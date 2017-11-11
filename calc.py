def wind_speed(u, v, w=0):
    """Calculates wind speed from u, v and w components."""
    return sqrt(u * u + v * v + w * w)
def get_wind_direction(u, v):
    return 90 - atan2(u, v)