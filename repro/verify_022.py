"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a Graph class and a Dijkstra implementation to find the
shortest paths from a source node to all other nodes in a weighted graph
represented by an adjacency list.
"""

import heapq


class Graph:
    """
    Represents a directed graph using an adjacency list.
    """

    def __init__(self):
        """Initializes an empty graph."""
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        """
        Adds a directed edge from u to v with a given weight.

        Args:
            u: Starting node.
            v: Ending node.
            weight: Numeric weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def get_neighbors(self, u):
        """
        Returns neighbors of a given node.

        Args:
            u: The node to get neighbors for.

        Returns:
            A list of tuples (neighbor, weight).
        """
        return self.adjacency_list.get(u, [])


def dijkstra(graph, start_node):
    """
    Computes the shortest paths from start_node to all other reachable nodes.

    Args:
        graph: A Graph instance.
        start_node: The starting node for the algorithm.

    Returns:
        A dictionary mapping each reachable node to its shortest distance from the start node.
    """
    distances = {start_node: 0}
    priority_queue = [(0, start_node)]
    visited = set()

    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)

        if current_node in visited:
            continue
        visited.add(current_node)

        for neighbor, weight in graph.get_neighbors(current_node):
            distance = current_distance + weight

            if neighbor not in distances or distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def run_demo():
    """
    Demonstrates the Dijkstra algorithm with a sample graph.
    """
    g = Graph()
    g.add_edge('A', 'B', 4)
    g.add_edge('A', 'C', 2)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 10)
    g.add_edge('C', 'D', 3)
    g.add_edge('D', 'E', 7)
    g.add_edge('E', 'A', 8)

    start = 'A'
    print(f"Finding shortest paths from node: {start}")
    results = dijkstra(g, start)

    for node, dist in sorted(results.items()):
        print(f"Distance to {node}: {dist}")


if __name__ == "__main__":
    run_demo()
