import numpy as np

class Ant:
    def __init__(self, graph):
        self.graph = graph
        self.num_cities = len(graph)
        self.visited = [False] * self.num_cities
        self.tour = []
        self.distance = 0.0
    
    def calculate_distance(self):
        distance = 0
        num_cities = len(self.tour)
        for i in range(num_cities):
            distance += self.graph[self.tour[i % num_cities]][self.tour[(i + 1) % num_cities]]
        return distance
    
    def ant_algorithm(self, num_ants, num_iterations, pheromon_coef=0.5, alpha=1, beta=2):
        num_cities = self.num_cities
        pheromones = np.ones((num_cities, num_cities))
        best_distance = float('inf')
        best_tour = []
        
        for _ in range(num_iterations):
            ants = [Ant(self.graph) for _ in range(num_ants)]
            for ant in ants:
                start_city = np.random.choice(list(self.graph.keys()))
                ant.tour.append(start_city)
                ant.visited[start_city] = True
                for _ in range(num_cities - 1):
                    current_city = ant.tour[-1]
                    probabilities = []
                    for city, distance in self.graph[current_city].items():
                        if not ant.visited[city]:
                            pheromone = pheromones[current_city][city]
                            probabilities.append((city, (pheromone ** alpha) * ((1 / distance) ** beta)))
                    probabilities = np.array(probabilities)
                    probabilities[:, 1] /= np.sum(probabilities[:, 1])
                    next_city = int(np.random.choice(probabilities[:, 0], p=probabilities[:, 1]))
                    ant.tour.append(next_city)
                    ant.visited[next_city] = True
                ant.distance = ant.calculate_distance()
                if ant.distance < best_distance:
                    best_distance = ant.distance
                    best_tour = ant.tour
            pheromones *= (1 - pheromon_coef)
            for ant in ants:
                for i in range(num_cities):
                    pheromones[ant.tour[i % num_cities]][ant.tour[(i + 1) % num_cities]] += 1 / ant.distance
        return best_tour, best_distance
