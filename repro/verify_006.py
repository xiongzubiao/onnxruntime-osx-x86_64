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
    Represents a weighted directed graph using an adjacency list.
    """

    def __init__(self):
        """Initialize an empty graph."""
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int):
        """
        Add a weighted edge from node u to node v.

        Args:
            u: Source node.
            v: Destination node.
            weight: Weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))

    def dijkstra(self, start_node: str) -> Dict[str, float]:
        """
        Compute the shortest distances from start_node to all reachable nodes.

        Args:
            start_node: The node to start the search from.

        Returns:
            A dictionary mapping node names to their shortest distance from start_node.
        """
        # Distances initialized to infinity
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0
        
        # Priority queue stores (distance, node)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # If we found a longer path already, skip
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency_list[current_node]:
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
    
    # Adding edges (u, v, weight)
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
    distances = graph.dijkstra(start_node)

    for node, dist in distances.items():
        print(f"Distance to {node}: {dist}")


if __name__ == "__main__":
    run_demo()
