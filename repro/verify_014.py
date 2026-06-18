"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides an implementation of Dijkstra's algorithm for finding
the shortest paths between nodes in a graph represented by an adjacency list.
"""

import heapq


class Graph:
    """
    A class representing a weighted directed graph using an adjacency list.
    """

    def __init__(self):
        """
        Initialize an empty graph.
        """
        self.adjacency_list = {}

    def add_edge(self, u, v, weight):
        """
        Add a weighted edge to the graph.

        :param u: Starting node.
        :param v: Ending node.
        :param weight: Weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        self.adjacency_list[u].append((v, weight))

    def dijkstra(self, start_node):
        """
        Perform Dijkstra's algorithm to find the shortest path from start_node to all other nodes.

        :param start_node: The node to start the search from.
        :return: A dictionary mapping each node to its shortest distance from start_node.
        """
        # Ensure start_node is in the distance map
        distances = {start_node: 0}
        
        # Priority queue stores (distance, node)
        priority_queue = [(0, start_node)]

        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)

            # Standard Dijkstra optimization: skip if we've found a shorter path already
            if current_distance > distances.get(current_node, float('inf')):
                continue

            if current_node in self.adjacency_list:
                for neighbor, weight in self.adjacency_list[current_node]:
                    distance = current_distance + weight

                    if neighbor not in distances or distance < distances[neighbor]:
                        distances[neighbor] = distance
                        heapq.heappush(priority_queue, (distance, neighbor))

        return distances


if __name__ == "__main__":
    # Demonstration of the Dijkstra algorithm
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('D', 'E', 7)
    graph.add_edge('E', 'A', 8)

    start_node = 'A'
    results = graph.dijkstra(start_node)

    print(f"Shortest distances from node {start_node}:")
    for node in sorted(results.keys()):
        print(f"To {node}: {results[node]}")
