import numpy as np
import random

#The ants have the name "Carlos" for a references to "Padrinos magicos"
class AntColony:
    def __init__(self, dist_matrix, n_carlos_ants, n_iterations, death_pheromone, pheromone_importance=1, visibility=1):
        self.dist_matrix = dist_matrix
        self.pheromone = np.ones(self.dist_matrix.shape) / len(dist_matrix)
        self.n_carlos_ants = n_carlos_ants
        self.n_iterations = n_iterations
        self.death_pheromone = death_pheromone
        self.pheromone_importance = pheromone_importance 
        self.visibility = visibility

    def run(self):
        best_distance = float('inf')
        best_solution = []
        for i in range(self.n_iterations):
            all_solutions = self.gen_all_paths()
            self.spread_pheromone(all_solutions)
            best_solution_for_iteration = min(all_solutions, key=lambda x: x[1])
            if best_solution_for_iteration[1] < best_distance:
                best_distance = best_solution_for_iteration[1]
                best_solution = best_solution_for_iteration[0]
            self.pheromone *=(1 - self.death_pheromone)
        return best_solution, best_distance

    def gen_path_dist(self, path):
        total_distance = 0
        for i in range(len(path) - 1):
            total_distance += self.dist_matrix[path[i]][path[i + 1]]
        total_distance += self.dist_matrix[path[-1]][path[0]]
        return total_distance

    def gen_all_paths(self):
        all_paths = []
        for i in range(self.n_carlos_ants):
            path = self.gen_path(0)
            all_paths.append((path, self.gen_path_dist(path)))
        return all_paths

    def gen_path(self, start):
        path = []
        visited = set()
        visited.add(start)
        prev = start
        for i in range(len(self.dist_matrix) - 1):
            move = self.pick_move(self.pheromone[prev], self.dist_matrix[prev], visited)
            path.append(move)
            visited.add(move)
            prev = move
        path.append(start)
        return path

    def spread_pheromone(self, all_paths):
        for path, dist in all_paths:
            for move in range(len(path) - 1):
                self.pheromone[path[move]][path[move + 1]] += 1.0 / dist
                self.pheromone[path[move + 1]][path[move]] += 1.0 / dist

    def pick_move(self, pheromone, dist, visited):
        pheromone = np.copy(pheromone)
        pheromone[list(visited)] = 0

        row = pheromone ** self.pheromone_importance * ((1.0 / dist) ** self.visibility)
        norm_row = row / row.sum()
        move = np.random.choice(range(len(self.dist_matrix)), 1, p=norm_row)[0]
        return move

def main():
    dist_matrix = np.array([[np.inf, 2, 2, 5, 7],
                            [2, np.inf, 4, 8, 2],
                            [2, 4, np.inf, 1, 3],
                            [5, 8, 1, np.inf, 2],
                            [7, 2, 3, 2, np.inf]])
    # Config
    n_carlos_ants = 5
    n_iterations = 100
    death_pheromone = 0.5
    pheromone_importance = 1
    visibility = 2

    ant_colony = AntColony(dist_matrix, n_carlos_ants, n_iterations, death_pheromone, pheromone_importance, visibility)
    best_solution, best_distance = ant_colony.run()

    print("Mejor solucion encontrada por Carlos:", best_solution)
    print("Distancia recorrida por Carlos:", best_distance)

if __name__ == '__main__':
    main()