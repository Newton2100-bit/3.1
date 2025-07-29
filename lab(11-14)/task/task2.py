import heapq
import time
import signal
import sys



def sig_handler(*args):
    value = int(input('Do you really want to quit\n1. YES\n2. NO'))
    if value == 1:
        exit(0)

signal.signal(signal.SIGTERM,sig_handler)
signal.signal(signal.SIGINT,sig_handler)


def dijkstra_heap(graph, num_vertices, source):
    """
    Dijkstra's algorithm using min-heap (priority queue)

    Args:
        graph: Adjacency list representation where graph[i] contains (neighbor, weight) tuples
        num_vertices: Number of vertices in the graph
        source: Source vertex (0-indexed)

    Returns:
        distances: List of shortest distances from source to all vertices
        predecessors: List to reconstruct shortest paths
    """
    # Initialize distances to infinity and predecessor array
    distances = [float("inf")] * num_vertices
    predecessors = [-1] * num_vertices
    visited = [False] * num_vertices

    # Distance from source to itself is 0
    distances[source] = 0

    # Min-heap to store (distance, vertex) pairs
    min_heap = [(0, source)]

    while min_heap:
        # Extract vertex with minimum distance
        current_distance, current_vertex = heapq.heappop(min_heap)

        # Skip if vertex already processed
        if visited[current_vertex]:
            continue

        # Mark current vertex as visited
        visited[current_vertex] = True

        # Update distances to adjacent vertices
        for neighbor, weight in graph[current_vertex]:
            if not visited[neighbor]:
                new_distance = current_distance + weight

                # If we found a shorter path, update it
                if new_distance < distances[neighbor]:
                    distances[neighbor] = new_distance
                    predecessors[neighbor] = current_vertex
                    # Add to heap with updated distance
                    heapq.heappush(min_heap, (new_distance, neighbor))

    return distances, predecessors


def build_adjacency_list(num_vertices):
    """
    Build adjacency list from user input

    Args:
        num_vertices: Number of vertices in the graph

    Returns:
        graph: Adjacency list representation
    """
    graph = [[] for _ in range(num_vertices)]

    print(f"\nEnter edge weights (enter 0 for no edge):")
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:  # No self-loops
                while True:
                    try:
                        weight = float(input(f"Weight of edge from vertex {i} to vertex {j}: "))
                        break
                    except ValueError as e:
                        print('wrong input',file = sys.stderr)
                if weight > 0:  # Only add edge if weight is positive
                    graph[i].append((j, weight))

    return graph


def get_path(predecessors, source, destination):
    """
    Reconstruct path from source to destination using predecessors array

    Args:
        predecessors: Array of predecessors from Dijkstra's algorithm
        source: Source vertex
        destination: Destination vertex

    Returns:
        path: List representing the shortest path
    """
    path = []
    current = destination

    # Backtrack from destination to source
    while current != -1:
        path.append(current)
        current = predecessors[current]

    # Reverse to get path from source to destination
    path.reverse()

    # Return path only if it starts from source (reachable)
    return path if path[0] == source else []


def print_results(distances, predecessors, source, num_vertices):
    """
    Print the shortest distances and paths from source to all vertices
    """
    print(f"\nShortest distances from vertex {source}:")
    print("-" * 50)

    for vertex in range(num_vertices):
        if distances[vertex] == float("inf"):
            print(f"Vertex {vertex}: No path exists")
        else:
            path = get_path(predecessors, source, vertex)
            path_str = " -> ".join(map(str, path))
            print(f"Vertex {vertex}: Distance = {distances[vertex]}, Path = {path_str}")


def print_graph(graph, num_vertices):
    """
    Print the adjacency list representation of the graph
    """
    print(f"\nAdjacency List Representation:")
    print("-" * 30)
    for vertex in range(num_vertices):
        neighbors = ", ".join(
            [f"{neighbor}(weight:{weight})" for neighbor, weight in graph[vertex]]
        )
        print(f"Vertex {vertex}: {neighbors if neighbors else 'No outgoing edges'}")


def main():
    """
    Main function to handle input and run Dijkstra's algorithm with min-heap
    """
    print("=== Single Source Shortest Path - Dijkstra's Algorithm (Min-Heap) ===\n")

    # Get number of vertices
    num_vertices = int(input("Enter the number of vertices: "))

    # Build adjacency list
    graph = build_adjacency_list(num_vertices)

    # Display the graph structure
    print_graph(graph, num_vertices)

    # Get source vertex
    source = int(input(f"\nEnter the source vertex (0 to {num_vertices-1}): "))

    # Validate source vertex
    if source < 0 or source >= num_vertices:
        print("Invalid source vertex!")
        return

    # Record start time
    start_time = time.process_time()

    # Run Dijkstra's algorithm
    distances, predecessors = dijkstra_heap(graph, num_vertices, source)

    # Record end time
    end_time = time.process_time()

    # Print results
    print_results(distances, predecessors, source, num_vertices)

    # Print execution time
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nExecution time: {execution_time:.4f} milliseconds")


if __name__ == "__main__":
    main()
