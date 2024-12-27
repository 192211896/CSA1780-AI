def dfs(graph, visited, node):
    """Recursive function for Depth First Search."""
    if node not in visited:
        visited.append(node)
        for neighbor in graph[node]:
            dfs(graph, visited, neighbor)

def main():
    # User-defined graph input
    print("Enter the graph as adjacency list (e.g., A: B C D, B: A E):")
    graph = {}
    while True:
        line = input()
        if line.strip() == "":
            break
        node, neighbors = line.split(":")
        node = node.strip()
        neighbors = neighbors.strip().split()
        graph[node] = neighbors

    start_node = input("Enter the starting node for DFS: ").strip()

    # Perform DFS
    visited = []
    dfs(graph, visited, start_node)

    # Output the result
    print("DFS Traversal Order:", " -> ".join(visited))

if __name__ == "__main__":
    main()
