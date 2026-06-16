"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a robust implementation of Dijkstra's algorithm to find the
shortest paths from a source node to all other nodes in a weighted graph
represented by an adjacency list.
"""

import heapq
from typing import Dict, List, Tuple, Optional


class Graph:
    """
    A class representing a directed, weighted graph using an adjacency list.
    """

    def __init__(self):
        """Initializes an empty graph."""
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int):
        """
        Adds a directed edge from node u to node v with a given weight.

        Args:
            u: Starting node.
            v: Ending node.
            weight: Weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))

    def dijkstra(self, start_node: str) -> Dict[str, float]:
        """
        Computes the shortest paths from the start_node to all other reachable nodes.

        Args:
            start_node: The node to start the search from.

        Returns:
            A dictionary mapping each node to its shortest distance from the start_node.
        """
        # Initialize distances with infinity
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0

        # Priority queue for (distance, node)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If we found a longer path already, skip it
            if current_distance > distances[current_node]:
                continue

            # Explore neighbors
            for neighbor, weight in self.adjacency_list.get(current_node, []):
                distance = current_distance + weight

                # If a shorter path is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def run_demo():
    """
    Sets up a sample graph and demonstrates Dijkstra's algorithm.
    """
    graph = Graph()
    
    # Adding edges: (u, v, weight)
    edges = [
        ('A', 'B', 4),
        ('A', 'C', 2),
        ('B', 'C', 5),
        ('B', 'D', 10),
        ('C', 'D', 3),
        ('D', 'E', 7),
        ('E', 'A', 8)
    ]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)

    start_node = 'A'
    print(f"Computing shortest paths from node: {start_node}")
    
    shortest_paths = graph.dijkstra(start_node)
    
    for node, distance in sorted(shortest_paths.items()):
        print(f"Distance to {node}: {distance}")


if __name__ == '__main__':
    run_demo()
