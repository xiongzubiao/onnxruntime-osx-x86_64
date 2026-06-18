"""
Dijkstra's Shortest Path Algorithm implementation.
This module provides a function to find the shortest path from a source node
to all other nodes in a weighted graph represented as an adjacency list.
"""

import heapq

def dijkstra(adj_list, start_node):
    """
    Finds the shortest paths from the start_node to all other nodes in the graph.

    Args:
        adj_list (dict): Adjacency list where keys are node identifiers and values 
                         are lists of tuples (neighbor, weight).
        start_node: The starting node for the algorithm.

    Returns:
        dict: A dictionary mapping each node to its shortest distance from start_node.
    """
    # Initialize distances with infinity and the start node with zero
    distances = {node: float('inf') for node in adj_list}
    if start_node not in distances:
        distances[start_node] = 0
    else:
        distances[start_node] = 0
    
    # Priority queue to store nodes to visit: (distance, node)
    priority_queue = [(0, start_node)]
    
    while priority_queue:
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we found a longer path than already recorded, skip it
        if current_distance > distances.get(current_node, float('inf')):
            continue
            
        # Check neighbors
        for neighbor, weight in adj_list.get(current_node, []):
            distance = current_distance + weight
            
            # Ensure neighbor is in distances dict (for nodes only appearing as destinations)
            if neighbor not in distances:
                distances[neighbor] = float('inf')
                
            # If a shorter path is found, update and push to queue
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))
                
    return distances

if __name__ == "__main__":
    # Example Graph: Adjacency List
    # Nodes: A, B, C, D, E
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('C', 5), ('D', 10)],
        'C': [('D', 3)],
        'D': [('E', 7)],
        'E': []
    }
    
    source = 'A'
    print(f"Calculating shortest paths from node: {source}")
    results = dijkstra(graph, source)
    
    for node, dist in sorted(results.items()):
        print(f"Distance from {source} to {node}: {dist}")
