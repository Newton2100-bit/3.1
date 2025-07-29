import sys
import time


def dijkstra_matrix(graph, num_vertices, source):
    """
    Dijkstra's algorithm using adjacency matrix representation

    Args:
        graph: 2D adjacency matrix where graph[i][j] represents weight of edge from i to j
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

    # Process all vertices
    for _ in range(num_vertices):
        # Find the unvisited vertex with minimum distance
        min_distance = float("inf")
        min_vertex = -1

        for vertex in range(num_vertices):
            if not visited[vertex] and distances[vertex] < min_distance:
                min_distance = distances[vertex]
                min_vertex = vertex

        # If no vertex found, remaining vertices are unreachable
        if min_vertex == -1:
            break

        # Mark current vertex as visited
        visited[min_vertex] = True

        # Update distances to adjacent vertices
        for neighbor in range(num_vertices):
            # Check if there's an edge and vertex is unvisited
            if (
                graph[min_vertex][neighbor] != 0
                and not visited[neighbor]
                and distances[min_vertex] + graph[min_vertex][neighbor]
                < distances[neighbor]
            ):

                distances[neighbor] = (
                    distances[min_vertex] + graph[min_vertex][neighbor]
                )
                predecessors[neighbor] = min_vertex

    return distances, predecessors


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


def main():
    """
    Main function to handle input and run Dijkstra's algorithm
    """
    print(
        "=== Single Source Shortest Path - Dijkstra's Algorithm (Adjacency Matrix) ===\n"
    )

    # Get number of vertices
    num_vertices = int(input("Enter the number of vertices: "))
    # Initialize adjacency matrix
    graph = [[0 for _ in range(num_vertices)] for _ in range(num_vertices)]

    # Get edge weights
    print(f"\nEnter edge weights (enter 0 for no edge):")
    for i in range(num_vertices):
        for j in range(num_vertices):
            if i != j:  # No self-loops
                while True:
                    try:
                        weight = float(input(f"Weight of edge from vertex {i} to vertex {j}: "))
                        graph[i][j] = weight
                        break
                    except ValueError as e:
                        print('Wrong input')

    # Get source vertex
    source = int(input(f"\nEnter the source vertex (0 to {num_vertices-1}): "))

    # Validate source vertex
    if source < 0 or source >= num_vertices:
        print("Invalid source vertex!")
        return

    # Record start time
    start_time = time.time()

    # Run Dijkstra's algorithm
    distances, predecessors = dijkstra_matrix(graph, num_vertices, source)

    # Record end time
    end_time = time.time()

    # Print results
    print_results(distances, predecessors, source, num_vertices)

    # Print execution time
    execution_time = (end_time - start_time) * 1000  # Convert to milliseconds
    print(f"\nExecution time: {execution_time:.4f} milliseconds")


if __name__ == "__main__":
    main()
