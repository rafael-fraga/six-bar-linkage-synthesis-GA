import numpy as np

def calculate_fitness(trajectory, target_trajectory):
    return np.sum(np.abs(np.array(trajectory) - np.array(target_trajectory)))