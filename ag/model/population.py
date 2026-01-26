from model.chromosome import Chromosome
import numpy as np

class Population():
    def __init__(self, size):
        self.size = size
        self.chromosomes = [Chromosome() for _ in range(size)]

    def select(self, target_trajectory, num_parents):
        for chromo in self.chromosomes:
            chromo.update_fitness(target_trajectory)
        self.chromosomes.sort(key=lambda chromo: chromo.fitness)
        self.chromosomes = self.chromosomes[:num_parents]

    def insert_chromosome(self, chromosome=Chromosome()):
        self.chromosomes.append(chromosome)

    def crossover(self):
        parent1, parent2 = np.random.choice(self.chromosomes, 2, replace=False)
        child_data = []
        for p1_param, p2_param in zip(parent1.get_params()[4:], parent2.get_params()[4:]):
            if np.random.rand() < 0.5:
                child_data.append(p1_param)
            else:
                child_data.append(p2_param)
        child = Chromosome(data=child_data)
        return child

    def reproduce(self, mr=0.3):
        while len(self.chromosomes) < self.size:
            child = self.crossover()
            child.mutate(mutation_rate=mr)
            self.insert_chromosome(child)