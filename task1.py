import networkx as nx
import matplotlib.pyplot as plt


def get_social_graph():
    DG = nx.DiGraph()

    DG.add_nodes_from(
        ["Аліса", "Боб", "Чарлі", "Девід", "Єва", "Френк", "Грейс"])

    DG.add_edges_from([("Аліса", "Боб"), ("Аліса", "Девід"), ("Боб", "Чарлі"), ("Чарлі", "Девід"),
                       ("Чарлі", "Єва"), ("Девід", "Єва"), ("Девід",
                                                            "Френк"), ("Єва", "Френк"),
                       ("Єва", "Грейс"), ("Френк", "Грейс")])
    return DG


def show_graph(DG):
    options = {
        "node_color": "yellow",
        "edge_color": "lightblue",
        "node_size": 500,
        "width": 3,
        "with_labels": True,
        "arrows": True
    }
    pos = nx.circular_layout(DG)
    plt.figure(figsize=(8, 6))
    plt.title("Граф соціальної мережі")
    nx.draw(DG, pos, ** options)
    edge_labels = nx.get_edge_attributes(DG, 'weight')
    nx.draw_networkx_edge_labels(
        DG, pos, edge_labels=edge_labels)
    plt.show()


def show_graph_analytics(DG):
    print(f"Кількість вершин {DG.number_of_nodes()}")
    print(f"Кількість граней {DG.number_of_edges()}")
    print(f"Ступінь вершин {DG.degree()}")
    print(f"Ступінь центральності {nx.degree_centrality(DG)}")
    print(f"Близькість вузла {nx.closeness_centrality(DG)}")
    print(f"Посередництво вузла {nx.betweenness_centrality(DG)}")
    print(f"Найкоротший шлях між Алісою та Грейс {
          nx.shortest_path(DG, source="Аліса", target="Грейс")}")
    print(f"Обхід в ширину {list(nx.bfs_tree(DG, source='Аліса').edges())}")
    print(f"Обхід в глибину {list(nx.dfs_tree(DG, source='Аліса').edges())}")
    print(f"Сильно зв'язані вершини: {
          list(nx.strongly_connected_components(DG))}")


if __name__ == '__main__':
    DG = get_social_graph()
    show_graph_analytics(DG)
    show_graph(DG)
