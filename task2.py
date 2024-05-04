from task1 import get_social_graph, show_graph
from collections import deque
import networkx as nx


def dfs(graph, vertex, visited=None, result=[]):
    if visited is None:
        visited = set()
    visited.add(vertex)
    result.append(vertex)
    for neighbor in graph[vertex]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited, result)
    return result


def bfs(graph, start, result=[]):
    visited = set()
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            result.append(vertex)
            visited.add(vertex)
            queue.extend(set(graph[vertex]) - visited)
    return result


if __name__ == '__main__':
    DG = get_social_graph()

    adjacency_list = {node: list(DG.neighbors(node)) for node in DG.nodes()}
    print(f"Обхід в глибину dfs {dfs(adjacency_list, 'Аліса')}")
    print(f"Обхід в глибину nx {
          list(nx.dfs_tree(DG, source='Аліса').nodes())}")

    print(f"Обхід в ширину bfs {bfs(adjacency_list, 'Аліса')}")
    print(f"Обхід в ширину nx {
          list(nx.bfs_tree(DG, source='Аліса').nodes())}")

    show_graph(DG)
