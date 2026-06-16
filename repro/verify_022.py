"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a Graph class and a Dijkstra algorithm implementation
to find the shortest path between nodes in a weighted graph using an
adjacency list representation.
"""

import heapq


class Graph:
    """
    A simple directed graph represented using an adjacency list.
    """

    def __init__(self):
        """Initialize the graph with an empty adjacency list."""
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        """
        Add a weighted edge from node u to node v.

        Args:
            u: Starting node.
            v: Ending node.
            weight: The weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []

    def dijkstra(self, start_node):
        """
        Compute the shortest paths from start_node to all other reachable nodes.

        Args:
            start_node: The node to start the search from.

        Returns:
            A dictionary mapping each node to its shortest distance from start_node.
        """
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0
        
        # Priority queue stores (distance, node)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Nodes can be added to the PQ multiple times. 
            # We only process the first one (which has the shortest distance).
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency_list.get(current_node, []):
                distance = current_distance + weight

                # If a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def run_demo():
    """
    Demonstrates the Dijkstra algorithm with a sample graph.
    """
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('D', 'E', 8)
    graph.add_edge('E', 'A', 7)

    start_node = 'A'
    print(f"Computing shortest paths from node: {start_node}")
    shortest_distances = graph.dijkstra(start_node)

    for node, distance in shortest_distances.items():
        print(f"Distance to {node}: {distance}")


if __name__ == '__main__':
    run_demo()
