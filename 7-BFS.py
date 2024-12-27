from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    traversal = []

    while queue:
        node = queue.popleft()
        if node not in visited:
            visited.add(node)
            traversal.append(node)
            queue.extend(graph[node] - visited)  # Add unvisited neighbors to the queue

    return traversal

# User input for graph
def main():
    graph = {}
    print("Enter the graph as adjacency list (type 'done' to stop):")
    while True:
        line = input("Enter node and its neighbors (e.g., A B C): ").strip()
        if line.lower() == "done":
            break
        parts = line.split()
        node = parts[0]
        neighbors = set(parts[1:])
        graph[node] = neighbors

    start = input("Enter the starting node: ").strip()
    
    if start not in graph:
        print(f"Error: Starting node '{start}' is not in the graph!")
        return

    # Perform BFS and print result
    result = bfs(graph, start)
    print(f"BFS Traversal starting from '{start}': {' -> '.join(result)}")

if __name__ == "__main__":
    main()
