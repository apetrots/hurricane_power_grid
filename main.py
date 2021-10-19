import numpy
from scipy import stats

class Hurricane:
    def __init__(self, max_sustained_windspeed, radius_to_max_wind_speed, affected_radius):
        self.max_sustained_windspeed = max_sustained_windspeed # In nautical miles per hour, or knots (kt)
        self.radius_to_max_wind_speed = radius_to_max_wind_speed # In nautical miles (nm)
        self.affected_radius = affected_radius # effectively the size of the hurricane, radius of area affected by hurricane in nautical miles (nm)

def main():
    
