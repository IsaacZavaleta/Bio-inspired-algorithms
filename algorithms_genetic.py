import random

def selection(population):
    tournament_size = 3
    selected = []
    for _ in range(2):
        participants = random.sample(population, tournament_size)
        best = max(participants, key=fitness)
        selected.append(best)
    return selected

def mutate(chromosome, mutation_rate):
    for i in range(len(chromosome)):
        if random.random() < mutation_rate:
            chromosome[i] = 1 - chromosome[i]

def fitness(chromosome):
    x = int("".join(map(str, chromosome)), 2)
    return x ** 2

def generate_population(population_size, chromosome_length):
    return [[random.randint(0, 1) for _ in range(chromosome_length)] for _ in range(population_size)]

def crossover(parent1, parent2, chromosome_length):
    point = random.randint(1, chromosome_length - 1)
    child1 = parent1[:point] + parent2[point:]
    child2 = parent2[:point] + parent1[point:]
    return child1, child2

def genetic_algorithm(population_size,chromosome_length,iteraccion,mutation_rate):
    population = generate_population(population_size, chromosome_length)
    for generation in range(iteraccion):
        new_population = []
        
        while len(new_population) < population_size:
            parent1, parent2 = selection(population)
            child1, child2 = crossover(parent1, parent2, chromosome_length)

            mutate(child1,mutation_rate)
            mutate(child2,mutation_rate)

            new_population.extend([child1, child2])
        
        population = new_population[:population_size]
        
        best_chromosome = max(population, key=fitness)
        print(f"Iterraccion {generation+1}:\n\tMejor individuo: {best_chromosome}\n\tFitness: {fitness(best_chromosome)}")

def main():
    #Config
    population_size = 50
    chromosome_length = 7
    iteraccion = 22
    mutation_rate = 0.21
    genetic_algorithm(population_size,chromosome_length,iteraccion,mutation_rate)

if __name__ == '__main__':
    main()