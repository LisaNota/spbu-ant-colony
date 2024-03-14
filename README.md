# Ant Colony Optimization for Travelling Salesman Problem

This project implements the Ant Colony Optimization (ACO) algorithm to solve the Travelling Salesman Problem (TSP). The TSP involves finding the shortest possible route that visits each city exactly once and returns to the original city. ACO mimics the behavior of ants searching for food to find an optimal or near-optimal solution to the TSP.

## Project Structure

1. **Algorithm Implementation**:
    - The `ant.py` file contains the implementation of the Ant class, which represents an ant in the ACO algorithm.
    - The Ant class includes methods for initializing ants, calculating distances, and performing the ACO algorithm to find the shortest path.

2. **Graphical User Interface**:
    - The `graph_gui.py` file contains the `GraphGUI` class, which constructs a graphical interface for user interaction with the ACO algorithm.
    - This interface allows users to create graphs by specifying the number of vertices and edges and to initiate the ACO algorithm.

3. **Helper Functions**:
    - The `main.py` file contains the main function `main()`, which launches the user interface.
    - The `creating()` and `ant_solution()` functions are utilized for graph creation and finding the shortest path, respectively.

## How to Use the Project

1. Run the program by executing the `main.py` file.
2. Enter the number of vertices in the graph and input the weighted edges in the format `(vertex_1, vertex_2, weight); (vertex_1, vertex_2, weight); ...`, where vertices are numbers from 0 to (number of vertices - 1).
3. Click the "Create Graph" button to build the graph based on the input data.
4. Set the algorithm parameters: number of ants, pheromone evaporation coefficient, number of iterations, importance of pheromone, and importance of distance.
5. Click the "Compute Optimal Path" button to initiate the ACO algorithm and obtain the shortest path.
6. The resulting path and its length will be displayed on the screen.

## Dependencies

1. Python 3.x
2. Libraries:
    - `tkinter`
    - `matplotlib`
    - `networkx`
    - `numpy`

## Notes

- Ensure that the input graph is connected and that weighted edges are provided in the correct format for the algorithm to work effectively.
- Adjusting the algorithm parameters may affect the performance and quality of the solution, so experimentation may be required to find optimal settings.
