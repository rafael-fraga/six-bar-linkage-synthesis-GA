from controller.algorithm import GeneticAlgorithm
from model.chromosome import Chromosome

r = Chromosome(params='replica')
r.update_trajectory(resolution=100)
target_trajectory = r.trajectory.copy()

ga = GeneticAlgorithm(
    target_trajectory=target_trajectory, 
    stall_limit=10, 
    maximum_error=6, 
    population_size=300, 
    num_generation=500, 
    mutation_rate=0.2)
ga.run()