from model.population import Population
from datetime import datetime
import json

class GeneticAlgorithm:
    def __init__(self, target_trajectory, population_size=300, num_generation=200, mutation_rate=0.3, stall_limit=float('inf'), maximum_error=float('inf')):
        self.population = Population(population_size)
        self.generations = [self.population]
        self.fitness_history = [float('inf')]
        self.best_chromosome = None
        self.stall_count = 0

        self.target_trajectory = target_trajectory
        self.population_size = population_size
        self.num_generation = num_generation
        self.mutation_rate = mutation_rate
        self.stall_limit = stall_limit
        self.maximum_error = maximum_error

        self.log = {
            'population_size': population_size,
            'num_generation': num_generation,
            'mutation_rate': mutation_rate,
            'stall_limit': stall_limit,
            'maximum_error': maximum_error,
            'target_trajectory': target_trajectory,
            'best_chromosome': [],
            'generations': [],
            'fitness_history': [],
            'best_chromosome_trajectory': []
        }


        

    def evolve(self):
        self.population.select(self.target_trajectory, num_parents=self.population_size//2)

        # immigration
        if self.population.chromosomes[0].fitness == self.fitness_history[-1]:
            self.stall_count += 1
            if self.stall_count >= self.stall_limit:
                print("Stall limit reached. Introducing new chromosomes.")
                for _ in range(self.population_size // 3):
                    self.population.insert_chromosome()
                self.stall_count = 0
        else:
            self.stall_count = 0

        self.population.reproduce(mr=self.mutation_rate)
        self.generations.append(self.population)
        self.best_chromosome = self.population.chromosomes[0]

        print(f"Generation {len(self.generations)}: Best Fitness = {self.best_chromosome.fitness}")
        self.fitness_history.append(self.best_chromosome.fitness)

        self.log['generations'].append([chromo.get_params() for chromo in self.population.chromosomes])
        self.log['fitness_history'].append(self.best_chromosome.fitness)
        self.log['best_chromosome'] = self.best_chromosome.get_params()
        self.log['best_chromosome_trajectory'] = self.best_chromosome.trajectory

    def update_log(self):
        with open('./log.json', 'w') as f:
            text = json.dumps(self.log, indent=4)
            f.write(text)
        

    def run(self):
        for _ in range(self.num_generation):
            if _ % 10 == 0:
                self.update_log(); print("Log updated.")

            if self.best_chromosome and self.best_chromosome.fitness <= self.maximum_error:
                print("Maximum error threshold reached. Stopping evolution.")
                break
            self.evolve()