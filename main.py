import numpy as np
from scipy import stats
import math

class Hurricane:
    def simulate(self, point):
        K = 1.14 # Some constant > 1; closer to 1 = more conservative estimates of the speeds
        xi = K * self.max_sustained_windspeed
        psi = (1/radius_to_max_wind_speed) * np.log( K/(K-1) )
        # static_wind_field = if
    
    def __init__(self, max_sustained_windspeed, radius_to_max_wind_speed, affected_radius, path_points):
        self.max_sustained_windspeed = max_sustained_windspeed # In nautical miles per hour, or knots (kt). Average wind speed over 1 minute 10 m above surface.
        self.radius_to_max_wind_speed = radius_to_max_wind_speed # In nautical miles (nm)
        self.affected_radius = affected_radius # effectively the size of the hurricane, radius of area affected by hurricane in nautical miles (nm)
        self.path_points = path_points

def calculate_path_points(position, distance_per_time_step, direction, time_step_count):
    points = []
    for i in range(time_step_count):
        points.append(np.add(position, np.multiply(distance_per_time_step * i, direction)))
    return points

def normalized(vec):
    return vec / np.linalg.norm(vec)

def main():
    path_count = 20;
    time_step_count = 6
    time_step_duration = 2 # in hours
    sample_size = 5 # equivalent to N_0 in paper

    # "Simulate N_0 hurricanes at landfall"
    for hurr_idx in range(path_count):
        path = calculate_path_points( [0.0, 0.0], 5.0, normalized([0.0, 1.0]), time_step_count) # in degrees
        # simulate hurricane
        hurricane = Hurricane(10.0, 2.0, 3.0, path) 
        landfall_eye_pos = hurricane.path_points[0]
        pressure_diff = sqrt( (2.636 + 0.0394899 * landfall_eye_pos - np.log(hurricane.max_sustained_windspeed)) / 0.0005086 ) # in millibars
        holland_pressure_param = 1.38 + 0.00184 * pressure_diff - 0.00309*hurricane.max_sustained_windspeed
        for scenario in range(sample_size):
            land_decay_factor = np.random.lognormal(mean=-3.466, sigma=0.703, size=None) # "Take N_0 samples of a lognormal PDF with parameters to simulate the land decay factor"
            for path in range(path_count):
                for time_step in range(time_step_count):
                    eye_pos = hurricane.path_points[time_step]
                    new_pressure_diff = pressure_diff * math.exp(-land_decay_factor * (time_step * time_step_duration))
                    new_radius_to_max_wind_speed = math.exp(2.636 - 0.0005086 * new_pressure_diff**2 + 0.0394899 * eye_pos[1])



    print("Hello World!")

if __name__ == "__main__":
    main()
    
