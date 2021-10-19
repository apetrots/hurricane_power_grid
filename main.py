import numpy as np
from scipy import stats


class Hurricane:
    #def simulate():

    def __init__(self, max_sustained_windspeed, radius_to_max_wind_speed, affected_radius, path_points):
        self.max_sustained_windspeed = max_sustained_windspeed # In nautical miles per hour, or knots (kt)
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

    print(calculate_path_points( [0.0, 0.0], 5.0, normalized([0.0, 1.0]), time_step_count))

    print("Hello World!")

if __name__ == "__main__":
    main()
    
