"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a robust implementation of Dijkstra's algorithm to find the
shortest paths between nodes in a weighted graph represented by an adjacency list.
"""

import heapq
from typing import Dict, List, Tuple, Optional


class Graph:
    """
    A class representing a directed graph using an adjacency list.
    """

    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int):
        """
        Add a weighted edge from node u to node v.

        Args:
            u: Starting node identifier.
            v: Ending node identifier.
            weight: The weight of the edge (must be non-negative).
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))

    def dijkstra(self, start_node: str) -> Dict[str, int]:
        """
        Compute the shortest distances from the start_node to all other reachable nodes.

        Args:
            start_node: The node from which to start the search.

        Returns:
            A dictionary mapping node identifiers to their shortest distance from start_node.
        """
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0
        
        # Priority queue stores (distance, node)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Nodes can be added to the PQ multiple times with different distances.
            # We only process the one with the smallest distance.
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.adjacency_list[current_node]:
                distance = current_distance + weight

                # If a shorter path to neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return {node: (dist if dist != float('inf') else -1) for node, dist in distances.items()}


def main():
    """
    Demonstration of the Dijkstra algorithm implementation.
    """
    print("--- Dijkstra's Shortest Path Demo ---")
    
    graph = Graph()
    
    # Adding edges (node_from, node_to, weight)
    edges = [
        ("A", "B", 4),
        ("A", "C", 2),
        ("B", "C", 5),
        ("B", "D", 10),
        ("C", "D", 3),
        ("D", "E", 7),
        ("E", "A", 8)
    ]
    
    for u, v, w in edges:
        graph.add_edge(u, v, w)
        
    start_node = "A"
    results = graph.dijkstra(start_node)
    
    print(f"Shortest distances from node '{start_node}':")
    for node, distance in sorted(results.items()):
        status = f"{distance}" if distance != -1 else "Unreachable"
        print(f"  To {node}: {status}")


if __name__ == '__main__':
    main()
