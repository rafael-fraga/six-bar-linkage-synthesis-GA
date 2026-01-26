import numpy as np
from model.genome import Genome
from domain.kinematics import calculate_trajectory
from domain.fitness import calculate_fitness

class Chromosome():

    def __init__(self, params=None, data=None):
        self.J1x, self.J1y = 0,0
        self.J5x, self.J5y = -0.171, 0.203
        self.genome = Genome(params=params)
        if data is not None:
            self.genome.L56 = data[0]
            self.genome.L68 = data[1]
            self.genome.L87 = data[2]
            self.genome.L67 = data[3]
            self.genome.L32 = data[4]
            self.genome.L27 = data[5]
            self.genome.L24 = data[6]
            self.genome.L47 = data[7]
            self.genome.L14 = data[8]
            self.genome.J3x = data[9]
            self.genome.J3y = data[10]
        self.fitness = None
        self.trajectory = None

    def update_trajectory(self, resolution):
        self.trajectory = calculate_trajectory(self, resolution=resolution)

    def update_fitness(self, target_trajectory):
        resolution = len(target_trajectory)
        self.update_trajectory(resolution=resolution)
        self.fitness = calculate_fitness(self.trajectory, target_trajectory)

    def get_params(self):
        self.params = [
            self.J1x, self.J1y,
            self.J5x, self.J5y,
            self.genome.L56, self.genome.L68,
            self.genome.L87, self.genome.L67,
            self.genome.L32, self.genome.L27,
            self.genome.L24, self.genome.L47,
            self.genome.L14,
            self.genome.J3x, self.genome.J3y
        ]
        self.params = [float(p) for p in self.params]
        return self.params
    
    def mutate(self, mutation_rate=0.3):
        for param in vars(self.genome).keys():
            if np.random.rand() < mutation_rate:
                mutation_amount = np.random.uniform(-0.1, 0.1) * getattr(self.genome, param)
                setattr(self.genome, param, getattr(self.genome, param) + mutation_amount)