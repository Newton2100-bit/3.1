#include <iostream>
#include <vector>
#include <queue>
#include <climits>
#include <chrono>

using namespace std;
using namespace std::chrono;

// =============================================================================
// TASK 1: DIJKSTRA'S ALGORITHM USING ADJACENCY MATRIX (WITHOUT MIN-HEAP)
// =============================================================================

class DijkstraMatrix {
private:
    int vertices;                    // Number of vertices
    vector<vector<int>> adjMatrix;   // Adjacency matrix to store graph
    
public:
    // Constructor to initialize the graph
    DijkstraMatrix(int V) {
        vertices = V;
        // Initialize adjacency matrix with 0 (no edge)
        adjMatrix.resize(V, vector<int>(V, 0));
    }
    
    // Function to add edge to the graph
    void addEdge(int u, int v, int weight) {
        adjMatrix[u][v] = weight;  // Add edge from u to v with given weight
        // For undirected graph, also add edge from v to u
        // adjMatrix[v][u] = weight;  // Uncomment for undirected graph
    }
    
    // Function to find vertex with minimum distance that is not yet processed
    int findMinVertex(vector<int>& distance, vector<bool>& visited) {
        int minIndex = -1;
        int minValue = INT_MAX;
        
        // Check all vertices to find minimum distance vertex
        for (int v = 0; v < vertices; v++) {
            // If vertex is not visited and has smaller distance
            if (!visited[v] && distance[v] < minValue) {
                minValue = distance[v];
                minIndex = v;
            }
        }
        return minIndex;
    }
    
    // Main Dijkstra's algorithm function using adjacency matrix
    void dijkstraMatrix(int source) {
        cout << "\n=== TASK 1: DIJKSTRA WITH ADJACENCY MATRIX ===\n";
        
        // Initialize distances and visited array
        vector<int> distance(vertices, INT_MAX);  // Set all distances to infinity
        vector<bool> visited(vertices, false);    // Mark all vertices as unvisited
        vector<int> parent(vertices, -1);         // To store shortest path tree
        
        // Distance from source to itself is 0
        distance[source] = 0;
        
        // Process all vertices
        for (int count = 0; count < vertices - 1; count++) {
            // Find minimum distance vertex that is not yet processed
            int u = findMinVertex(distance, visited);
            
            // Mark the selected vertex as processed
            visited[u] = true;
            
            // Update distance of adjacent vertices of selected vertex
            for (int v = 0; v < vertices; v++) {
                // Update distance[v] if:
                // 1. There is an edge from u to v (adjMatrix[u][v] != 0)
                // 2. Vertex v is not visited
                // 3. Total weight from source to v through u is smaller than current distance[v]
                if (adjMatrix[u][v] != 0 && !visited[v] && 
                    distance[u] != INT_MAX && 
                    distance[u] + adjMatrix[u][v] < distance[v]) {
                    
                    distance[v] = distance[u] + adjMatrix[u][v];
                    parent[v] = u;  // Update parent for path reconstruction
                }
            }
        }
        
        // Print the shortest distances
        printSolution(distance, parent, source);
    }
    
    // Function to print the shortest path from source to destination
    void printPath(vector<int>& parent, int destination) {
        if (parent[destination] == -1) {
            cout << destination;
            return;
        }
        printPath(parent, parent[destination]);
        cout << " -> " << destination;
    }
    
    // Function to print the solution
    void printSolution(vector<int>& distance, vector<int>& parent, int source) {
        cout << "Shortest distances from source vertex " << source << ":\n";
        cout << "Vertex\t\tDistance\tPath\n";
        
        for (int i = 0; i < vertices; i++) {
            cout << i << "\t\t";
            if (distance[i] == INT_MAX) {
                cout << "INF\t\tNo path";
            } else {
                cout << distance[i] << "\t\t";
                printPath(parent, i);
            }
            cout << endl;
        }
    }
};

// =============================================================================
// TASK 2: DIJKSTRA'S ALGORITHM USING MIN-HEAP (PRIORITY QUEUE)
// =============================================================================

class DijkstraHeap {
private:
    int vertices;                           // Number of vertices
    vector<vector<pair<int, int>>> adjList; // Adjacency list: {destination, weight}
    
public:
    // Constructor to initialize the graph
    DijkstraHeap(int V) {
        vertices = V;
        adjList.resize(V);
    }
    
    // Function to add edge to the graph
    void addEdge(int u, int v, int weight) {
        // Add edge from u to v with given weight
        adjList[u].push_back({v, weight});
        // For undirected graph, also add edge from v to u
        // adjList[v].push_back({u, weight});  // Uncomment for undirected graph
    }
    
    // Main Dijkstra's algorithm function using min-heap
    void dijkstraHeap(int source) {
        cout << "\n=== TASK 2: DIJKSTRA WITH MIN-HEAP ===\n";
        
        // Initialize distances and parent array
        vector<int> distance(vertices, INT_MAX);  // Set all distances to infinity
        vector<int> parent(vertices, -1);         // To store shortest path tree
        
        // Min-heap to store {distance, vertex}
        // Priority queue in C++ is max-heap by default, so we use greater<> for min-heap
        priority_queue<pair<int, int>, vector<pair<int, int>>, greater<pair<int, int>>> pq;
        
        // Distance from source to itself is 0
        distance[source] = 0;
        pq.push({0, source});  // Push {distance, vertex}
        
        // Process all vertices
        while (!pq.empty()) {
            // Extract vertex with minimum distance
            int u = pq.top().second;
            int dist = pq.top().first;
            pq.pop();
            
            // Skip if we've already found a better path
            if (dist > distance[u]) continue;
            
            // Check all adjacent vertices of u
            for (auto& edge : adjList[u]) {
                int v = edge.first;      // Adjacent vertex
                int weight = edge.second; // Weight of edge u->v
                
                // If shorter path to v is found through u
                if (distance[u] + weight < distance[v]) {
                    distance[v] = distance[u] + weight;
                    parent[v] = u;
                    pq.push({distance[v], v});  // Add to priority queue
                }
            }
        }
        
        // Print the shortest distances
        printSolution(distance, parent, source);
    }
    
    // Function to print the shortest path from source to destination
    void printPath(vector<int>& parent, int destination) {
        if (parent[destination] == -1) {
            cout << destination;
            return;
        }
        printPath(parent, parent[destination]);
        cout << " -> " << destination;
    }
    
    // Function to print the solution
    void printSolution(vector<int>& distance, vector<int>& parent, int source) {
        cout << "Shortest distances from source vertex " << source << ":\n";
        cout << "Vertex\t\tDistance\tPath\n";
        
        for (int i = 0; i < vertices; i++) {
            cout << i << "\t\t";
            if (distance[i] == INT_MAX) {
                cout << "INF\t\tNo path";
            } else {
                cout << distance[i] << "\t\t";
                printPath(parent, i);
            }
            cout << endl;
        }
    }
};

// =============================================================================
// MAIN FUNCTION - USER INTERACTION AND TESTING
// =============================================================================

int main() {
    int vertices, source;
    
    cout << "=== SINGLE SOURCE SHORTEST PATH PROBLEM ===\n";
    cout << "=== EXPERIMENT 12: DIJKSTRA'S ALGORITHM ===\n\n";
    
    // Input number of vertices
    cout << "Enter number of vertices in the graph: ";
    cin >> vertices;
    
    // Create objects for both implementations
    DijkstraMatrix graphMatrix(vertices);
    DijkstraHeap graphHeap(vertices);
    
    // Input edges
    cout << "\nEnter edges (enter -1 -1 -1 to stop):\n";
    cout << "Format: source_vertex destination_vertex weight\n";
    
    int u, v, weight;
    while (true) {
        cout << "Enter edge (from to weight): ";
        cin >> u >> v >> weight;
        
        // Stop condition
        if (u == -1 && v == -1 && weight == -1) break;
        
        // Validate input
        if (u < 0 || u >= vertices || v < 0 || v >= vertices) {
            cout << "Invalid vertices! Please enter vertices between 0 and " << vertices-1 << endl;
            continue;
        }
        
        if (weight < 0) {
            cout << "Warning: Negative weight detected! Dijkstra's algorithm doesn't work with negative weights.\n";
        }
        
        // Add edge to both graphs
        cout << "Adding edge: " << u << " -> " << v << " (weight: " << weight << ")\n";
        graphMatrix.addEdge(u, v, weight);
        graphHeap.addEdge(u, v, weight);
    }
    
    // Input source vertex
    cout << "\nEnter source vertex: ";
    cin >> source;
    
    // Validate source vertex
    if (source < 0 || source >= vertices) {
        cout << "Invalid source vertex!\n";
        return 1;
    }
    
    cout << "\n" << string(60, '=') << "\n";
    cout << "RUNNING DIJKSTRA'S ALGORITHM...\n";
    cout << string(60, '=') << "\n";
    
    // Run Task 1: Dijkstra with adjacency matrix
    auto start1 = high_resolution_clock::now();
    graphMatrix.dijkstraMatrix(source);
    auto end1 = high_resolution_clock::now();
    auto duration1 = duration_cast<microseconds>(end1 - start1);
    
    cout << "\n" << string(60, '-') << "\n";
    
    // Run Task 2: Dijkstra with min-heap
    auto start2 = high_resolution_clock::now();
    graphHeap.dijkstraHeap(source);
    auto end2 = high_resolution_clock::now();
    auto duration2 = duration_cast<microseconds>(end2 - start2);
    
    // Performance comparison
    cout << "\n" << string(60, '=') << "\n";
    cout << "PERFORMANCE COMPARISON:\n";
    cout << string(60, '=') << "\n";
    cout << "Task 1 (Adjacency Matrix): " << duration1.count() << " microseconds\n";
    cout << "Task 2 (Min-Heap): " << duration2.count() << " microseconds\n";
    cout << "Difference: " << abs(duration1.count() - duration2.count()) << " microseconds\n";
    
    if (duration1.count() < duration2.count()) {
        cout << "Adjacency Matrix approach was faster by " 
             << (duration2.count() - duration1.count()) << " microseconds\n";
    } else {
        cout << "Min-Heap approach was faster by " 
             << (duration1.count() - duration2.count()) << " microseconds\n";
    }
    
    cout << "\nNote: Min-heap approach is generally faster for sparse graphs (fewer edges)\n";
    cout << "Adjacency matrix approach might be faster for dense graphs (many edges)\n";
    
    return 0;
}

/* 
SAMPLE INPUT FOR TESTING:
=========================

Example 1: Simple graph
Vertices: 5
Edges:
0 1 10
0 4 5
1 2 1
1 4 2
2 3 4
3 2 6
3 0 7
4 1 3
4 2 9
4 3 2
-1 -1 -1
Source: 0

Example 2: Another test case
Vertices: 4
Edges:
0 1 1
0 2 4
1 2 2
1 3 5
2 3 1
-1 -1 -1
Source: 0

TIME COMPLEXITY:
================
Task 1 (Adjacency Matrix): O(V²) where V is number of vertices
Task 2 (Min-Heap): O((V + E) log V) where V is vertices and E is edges

SPACE COMPLEXITY:
=================
Task 1: O(V²) for adjacency matrix
Task 2: O(V + E) for adjacency list
*/
