import numpy as np

def calculate_fitness(trajectory, target_trajectory):
    if np.isnan(trajectory).any():
        return np.inf
    return np.sum(np.abs(np.array(trajectory) - np.array(target_trajectory)))