from collections import deque

def water_jug_solver(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque()
    solutions = []
    
    # Start with both jugs empty
    queue.append((0, 0))
    
    while queue:
        jug1, jug2 = queue.popleft()
        
        # Check if we've already visited this state
        if (jug1, jug2) in visited:
            continue
        
        # Mark as visited
        visited.add((jug1, jug2))
        solutions.append((jug1, jug2))
        
        # Check if we've reached the target
        if jug1 == target or jug2 == target:
            print("Solution found!")
            for step in solutions:
                print(step)
            return
        
        # Generate possible next states
        # Fill Jug1
        queue.append((jug1_capacity, jug2))
        # Fill Jug2
        queue.append((jug1, jug2_capacity))
        # Empty Jug1
        queue.append((0, jug2))
        # Empty Jug2
        queue.append((jug1, 0))
        # Pour Jug1 -> Jug2
        pour_to_jug2 = min(jug1, jug2_capacity - jug2)
        queue.append((jug1 - pour_to_jug2, jug2 + pour_to_jug2))
        # Pour Jug2 -> Jug1
        pour_to_jug1 = min(jug2, jug1_capacity - jug1)
        queue.append((jug1 + pour_to_jug1, jug2 - pour_to_jug1))
    
    print("No solution found.")

# User-defined input
if __name__ == "__main__":
    jug1_capacity = int(input("Enter capacity of Jug 1: "))
    jug2_capacity = int(input("Enter capacity of Jug 2: "))
    target = int(input("Enter the target amount of water: "))
    
    if target > max(jug1_capacity, jug2_capacity):
        print("Target cannot be greater than the largest jug capacity.")
    else:
        water_jug_solver(jug1_capacity, jug2_capacity, target)
n
