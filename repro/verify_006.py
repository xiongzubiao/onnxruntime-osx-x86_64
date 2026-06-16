"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a robust implementation of Dijkstra's algorithm for finding
the shortest paths between nodes in a graph, which may represent, for example,
road networks.
"""

import heapq


class Graph:
    """
    A class representing a directed, weighted graph using an adjacency list.
    """

    def __init__(self):
        """Initializes an empty graph."""
        self.nodes = set()
        self.edges = {}

    def add_node(self, value):
        """Adds a node to the graph."""
        self.nodes.add(value)
        if value not in self.edges:
            self.edges[value] = []

    def add_edge(self, from_node, to_node, weight):
        """Adds a directed, weighted edge to the graph."""
        self.add_node(from_node)
        self.add_node(to_node)
        self.edges[from_node].append((to_node, weight))


def dijkstra(graph, start_node):
    """
    Computes the shortest paths from a start node to all other nodes.

    Args:
        graph: The Graph instance to search.
        start_node: The starting node identifier.

    Returns:
        A dictionary mapping each node to its shortest distance from the start node.
    """
    distances = {node: float('infinity') for node in graph.nodes}
    distances[start_node] = 0
    priority_queue = [(0, start_node)]

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        # Nodes can be added to the priority queue multiple times.
        # We only process the one with the smallest distance.
        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph.edges[current_node]:
            distance = current_distance + weight

            # Only consider this new path if it's better than any path we've
            # already found.
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def run_demo():
    """
    Sets up a sample graph and demonstrates the Dijkstra algorithm.
    """
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'D', 3)
    g.add_edge('D', 'E', 7)
    g.add_edge('E', 'A', 8)

    start_node = 'A'
    distances = dijkstra(g, start_node)

    print(f"Shortest distances from node '{start_node}':")
    for node, distance in sorted(distances.items()):
        print(f"Node {node}: {distance}")


if __name__ == '__main__':
    run_demo()
