"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a robust implementation of Dijkstra's algorithm to find the 
shortest paths from a source node to all other nodes in a weighted graph 
represented by an adjacency list.
"""

import heapq

class Graph:
    """
    A class representing a directed, weighted graph using an adjacency list.
    """
    def __init__(self):
        """
        Initialize the graph with an empty adjacency list.
        """
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        """
        Add a directed edge to the graph.

        Args:
            u: Starting node.
            v: Ending node.
            weight: Weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

def dijkstra(graph, start_node):
    """
    Compute the shortest paths from a start node using Dijkstra's algorithm.

    Args:
        graph: An instance of the Graph class.
        start_node: The node to start the search from.

    Returns:
        A dictionary containing the shortest distance from the start node to every other node.
    """
    distances = {node: float('inf') for node in graph.adjacency_list}
    # Ensure start_node is in distances even if it has no outgoing edges
    if start_node not in distances:
        distances[start_node] = float('inf')
    
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.adjacency_list.get(current_node, []):
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances

def run_demo():
    """
    Set up a sample graph and run Dijkstra's algorithm to demonstrate functionality.
    """
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'E', 3)
    g.add_edge('E', 'D', 4)
    g.add_edge('D', 'F', 11)

    start_node = 'A'
    distances = dijkstra(g, start_node)

    print(f"Shortest distances from node {start_node}:")
    for node, distance in sorted(distances.items()):
        print(f"Node {node}: {distance}")

if __name__ == '__main__':
    run_demo()
