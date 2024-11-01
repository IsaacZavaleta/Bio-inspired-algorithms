import numpy as np

def function(x):
    return x**2

def simulated_annealing(function, limits, temperature, cooling_rate, interactions):
    solution_current = np.random.uniform(limits[0], limits[1])
    cost_current = function(solution_current)
    
    solution_best = solution_current
    cost_best = cost_current

    for i in range(interactions):
        candidate_solution = solution_current + np.random.uniform(-0.1, 0.1)
        
        candidate_solution = np.clip(candidate_solution, limits[0], limits[1])
        candidate_cost = function(candidate_solution)
        
        delta_cost = candidate_cost - cost_current

        if delta_cost < 0 or np.exp(-delta_cost / temperature) > np.random.rand():
            solution_current, cost_current = candidate_solution, candidate_cost
        
        if cost_current < cost_best:
            solution_best, cost_best = solution_current, cost_current
        
        temperature *= cooling_rate
    
    return solution_best, cost_best

def main():
    #Config
    limits = [-10, 10]
    temperature = 10  
    cooling_rate = 0.99
    interactions = 1000  

    
    solution_best, cost_best = simulated_annealing(function, limits, temperature, cooling_rate, interactions)
    print(f"La mejor solución para la configuracion: {solution_best}, con el costo: {cost_best}")

if __name__ == '__main__':
    main()