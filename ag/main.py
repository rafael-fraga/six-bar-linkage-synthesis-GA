from model.chromosome import Chromosome
from model.population import Population

r = Chromosome(params='replica')
r.update_trajectory()

pop = Population(size=300)
gen, stall_count, best_fitness = 0, 0, float('inf')
while True:
    fitness_array = [c.fitness for c in pop.chromosomes]
    pop.select(target_trajectory=r.trajectory, num_parents=60, resolution=100)

    # immigration
    immigration_str = ''
    if fitness_array[0] == best_fitness:
        stall_count += 1
        if stall_count >= 15:
            for _ in range(100):
                pop.insert_chromosome(Chromosome())
            stall_count = 0
            immigration_str = ' - Immigrants Added'

    pop.reproduce(mr=0.75)
    best_fitness = pop.chromosomes[0].fitness

    gen += 1
    with open("best_chromosome", "w") as f:
        f.write(str(pop.chromosomes[0].get_params()).replace('[', '').replace(']', ''))
    print(f"Generation: {gen} | Best Fitness: {best_fitness} | Population Size: {len(pop.chromosomes)}" + immigration_str)