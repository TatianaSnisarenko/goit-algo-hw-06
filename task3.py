from task1 import get_social_graph, show_graph
from collections import deque
import networkx as nx
import matplotlib.pyplot as plt


def add_weights_to_graph(G):
    weights = {("Аліса", "Боб"): 5, ("Аліса", "Девід"): 3,
               ("Боб", "Чарлі"): 2, ("Чарлі", "Девід"): 1,
               ("Чарлі", "Єва"): 4, ("Девід", "Єва"): 2,
               ("Девід", "Френк"): 3, ("Єва", "Френк"): 1,
               ("Єва", "Грейс"): 2, ("Френк", "Грейс"): 4}

    for edge, weight in weights.items():
        G.add_edge(*edge, weight=weight)


def graph_to_dict(G):
    result = {}
    for node in G.nodes():
        neighbors = {}
        for neighbor, data in G[node].items():
            neighbors[neighbor] = data['weight']
        result[node] = neighbors
    return result


def dijkstra(graph, start):
    distances = {vertex: float('infinity') for vertex in graph}
    distances[start] = 0
    unvisited = list(graph.keys())

    while unvisited:
        current_vertex = min(unvisited, key=lambda vertex: distances[vertex])

        if distances[current_vertex] == float('infinity'):
            break

        for neighbor, weight in graph[current_vertex].items():
            distance = distances[current_vertex] + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance

        unvisited.remove(current_vertex)

    return distances


if __name__ == '__main__':
    DG = get_social_graph()
    add_weights_to_graph(DG)

    graph = graph_to_dict(DG)
    print(f"Найкоротші шляхи між вершинами dijkstra: {
          dijkstra(graph, 'Аліса')}")

    shortest_paths = nx.single_source_dijkstra_path_length(DG, source="Аліса")
    print(f"Найкоротші шляхи між вершинами nx: {shortest_paths}")

    show_graph(DG)
