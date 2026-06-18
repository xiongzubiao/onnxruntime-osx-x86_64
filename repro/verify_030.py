"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a complete, runnable implementation of Dijkstra's algorithm
for finding the shortest paths from a single source node to all other nodes
in a weighted graph represented as an adjacency list.
"""

import heapq
from typing import Dict, List, Tuple, Optional


class DijkstraSolver:
    """
    A class to solve the single-source shortest path problem using Dijkstra's algorithm.
    """

    def __init__(self, adjacency_list: Dict[str, List[Tuple[str, int]]]):
        """
        Initializes the solver with a graph adjacency list.

        Args:
            adjacency_list (Dict[str, List[Tuple[str, int]]]): A dictionary where keys are node names
                and values are lists of (neighbor, weight) tuples.
        """
        self.graph = adjacency_list

    def find_shortest_paths(self, start_node: str) -> Dict[str, float]:
        """
        Computes the shortest distance from the start_node to all reachable nodes.

        Args:
            start_node (str): The starting node.

        Returns:
            Dict[str, float]: A dictionary mapping each node to its shortest distance from start_node.
                Nodes not reachable are not included or can be represented as infinity.
        """
        # distances[node] = shortest distance from start_node to node
        distances = {node: float('inf') for node in self.graph}
        distances[start_node] = 0

        # Priority queue stores (distance, node)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Nodes can be added multiple times to the PQ; only process the shortest one
            if current_distance > distances[current_node]:
                continue

            for neighbor, weight in self.graph.get(current_node, []):
                distance = current_distance + weight

                # If a shorter path to neighbor is found
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))

        return distances


def run_demo():
    """
    Demonstrates the DijkstraSolver with a sample weighted graph.
    """
    # Sample graph adjacency list
    # A --1--> B --2--> C
    # A --4--> C
    # B --1--> D
    # D --3--> C
    graph_data = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 1)],
        'C': [('A', 4), ('B', 2), ('D', 3)],
        'D': [('B', 1), ('C', 3)]
    }

    solver = DijkstraSolver(graph_data)
    start_node = 'A'
    results = solver.find_shortest_paths(start_node)

    print(f"Shortest distances from node '{start_node}':")
    for node, distance in sorted(results.items()):
        print(f"  To {node}: {distance}")


if __name__ == '__main__':
    run_demo()
