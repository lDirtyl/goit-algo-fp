import heapq
import networkx as nx
import matplotlib.pyplot as plt

# Створення власного вагового графа
G = nx.Graph()
G.add_edge("A", "B", weight=1)
G.add_edge("B", "C", weight=2)
G.add_edge("C", "D", weight=3)

# Реалізація алгоритму Дейкстри
def dijkstra(graph, start):
    shortest_paths = {vertex: float('infinity') for vertex in graph}
    previous_nodes = {vertex: None for vertex in graph}
    shortest_paths[start] = 0
    priority_queue = [(0, start)]

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        # Пропускаємо обробку, якщо знайшли більш короткий шлях
        if current_distance > shortest_paths[current_vertex]:
            continue

        for neighbor, attributes in graph[current_vertex].items():
            distance = attributes["weight"]
            new_distance = current_distance + distance

            if new_distance < shortest_paths[neighbor]:
                shortest_paths[neighbor] = new_distance
                previous_nodes[neighbor] = current_vertex
                heapq.heappush(priority_queue, (new_distance, neighbor))

    return shortest_paths, previous_nodes

# Використання алгоритму Дейкстри
shortest_paths, previous_nodes = dijkstra(G, "A")
print("Найкоротші шляхи від A:", shortest_paths)

# Візуалізація графа
pos = nx.spring_layout(G)  # Позиції для всіх вершин
nx.draw_networkx_nodes(G, pos, node_size=700)
nx.draw_networkx_edges(G, pos, width=2)
edge_labels = nx.get_edge_attributes(G, 'weight')
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
nx.draw_networkx_labels(G, pos, font_size=20, font_family="sans-serif")

plt.axis("off")
plt.show()
