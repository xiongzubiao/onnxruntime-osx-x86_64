"""
Dijkstra's Shortest Path Algorithm Implementation.

This module provides a complete, runnable implementation of Dijkstra's algorithm
for finding the shortest paths from a single source vertex to all other vertices
in a weighted graph represented as an adjacency list.
"""

import heapq
from typing import Dict, List, Tuple

class Graph:
    """
    A class representing a directed, weighted graph using an adjacency list.
    """
    def __init__(self):
        """Initializes an empty graph."""
        self.adjacency_list: Dict[str, List[Tuple[str, int]]] = {}

    def add_edge(self, u: str, v: str, weight: int):
        """
        Adds a directed edge from vertex u to vertex v with the given weight.
        
        Args:
            u: Starting vertex.
            v: Ending vertex.
            weight: Weight of the edge.
        """
        if u not in self.adjacency_list:
            self.adjacency_list[u] = []
        if v not in self.adjacency_list:
            self.adjacency_list[v] = []
        self.adjacency_list[u].append((v, weight))

    def dijkstra(self, start_node: str) -> Dict[str, float]:
        """
        Computes the shortest distance from start_node to all other reachable nodes.
        
        Args:
            start_node: The source vertex for pathfinding.
            
        Returns:
            A dictionary mapping each node to its shortest distance from start_node.
        """
        distances = {node: float('inf') for node in self.adjacency_list}
        distances[start_node] = 0
        
        priority_queue = [(0, start_node)]
        
        while priority_queue:
            current_distance, current_node = heapq.heappop(priority_queue)
            
            if current_distance > distances[current_node]:
                continue
                
            for neighbor, weight in self.adjacency_list.get(current_node, []):
                distance = current_distance + weight
                
                if distance < distances[neighbor]:
                    distances[neighbor] = distance
                    heapq.heappush(priority_queue, (distance, neighbor))
                    
        return distances

def run_demo():
    """
    Sets up a sample graph and demonstrates the Dijkstra implementation.
    """
    graph = Graph()
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'C', 2)
    graph.add_edge('B', 'C', 5)
    graph.add_edge('B', 'D', 10)
    graph.add_edge('C', 'D', 3)
    graph.add_edge('C', 'E', 8)
    graph.add_edge('D', 'E', 2)
    
    start_node = 'A'
    print(f"Computing shortest paths from node: {start_node}")
    distances = graph.dijkstra(start_node)
    
    for node, dist in sorted(distances.items()):
        print(f"Distance to {node}: {dist}")

if __name__ == '__main__':
    run_demo()
