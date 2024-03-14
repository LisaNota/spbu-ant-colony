import tkinter as tk
import networkx as nx
from matplotlib.axes import Axes
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from graph_gui import GraphGUI
from ant import Ant

options = {
    'node_color': '#D3D3D3',
    'node_size': 300,
    'width': 1,
    'arrowstyle': '-|>',
    'arrowsize': 10,
    'edge_color': 'black',
    'font_size': 12,
}
pos = None        
        
def creating(cnt_vertices: int, edges: str, ax, canvas_widget) -> None:
    global options, pos

    edges = ''.join(edges).split(';')
    edges = [edge.strip() for edge in edges]
    weighted_edges = [eval(edge) for edge in edges]
    vertices = list(range(cnt_vertices))
    
    G = nx.DiGraph(directed=True)
    G.add_nodes_from(vertices)
    G.add_weighted_edges_from(weighted_edges)

    pos = nx.circular_layout(G)
    nx.draw(G, ax=ax, pos=pos, with_labels=True, arrows=True, **options)

    canvas_widget.draw()

def ant_solution(edges: list, num_ants: int, pheromon_coef: float, iterations: int, alpha: float, beta: float, txt_way: tk.Text, txt_len: tk.Text, ax_2: Axes, canvas_widget_2: FigureCanvasTkAgg) -> None:
    global options, pos
    edges = ''.join(edges).split(';')
    edges = [edge.strip() for edge in edges]
    weighted_edges = [eval(edge) for edge in edges]
    graph = {}
    for edge in weighted_edges:
        if edge[0] not in graph:
            graph[edge[0]] = {}
        if edge[1] not in graph:
            graph[edge[1]] = {}
        graph[edge[0]][edge[1]] = edge[2]
    
    solution = Ant(graph)
    best_path, best_len = solution.ant_algorithm(num_ants, iterations, pheromon_coef, alpha, beta)
    
    txt_way.config(state='normal')
    txt_way.insert(tk.END, best_path)
    txt_way.config(state='disabled')
    
    txt_len.config(state='normal')
    txt_len.insert(tk.END, best_len)
    txt_len.config(state='disabled')
    
    F = nx.DiGraph(directed=True)
    best_path.append(best_path[0])
    F.add_nodes_from(best_path)
    
    for i in range(len(best_path)-1):
        F.add_edge(best_path[i], best_path[i+1])

    nx.draw(F, ax=ax_2, pos=pos, with_labels=True, arrows=True, **options)

    canvas_widget_2.draw()

if __name__ == "__main__":
  root = tk.Tk()
  app = GraphGUI(root)
  app.set_calculating_command(lambda edges, num_ants, pheromon_coef, iterations, alpha, beta, txt_way, txt_len: ant_solution
                          (edges, num_ants, pheromon_coef, iterations, alpha, beta, txt_way, txt_len, app.ax_2, app.canvas_widget_2))
  app.set_creating_command(lambda cnt_vertices, edges: creating(cnt_vertices, edges, app.ax, app.canvas_widget))
  root.mainloop()
