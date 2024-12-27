from collections import deque

def is_valid_state(state, missionaries, cannibals):
    """Check if a state is valid."""
    m_left, c_left, boat, m_right, c_right = state
    
    # Conditions to ensure no side has more cannibals than missionaries
    if (m_left > 0 and c_left > m_left) or (m_right > 0 and c_right > m_right):
        return False

    # Ensure the number of people on each side is within bounds
    if not (0 <= m_left <= missionaries and 0 <= c_left <= cannibals):
        return False

    return True

def get_next_states(state, missionaries, cannibals):
    """Generate all possible valid states from the current state."""
    m_left, c_left, boat, m_right, c_right = state
    next_states = []

    # Possible moves for the boat (1 or 2 people)
    moves = [(1, 0), (0, 1), (1, 1), (2, 0), (0, 2)]

    for m, c in moves:
        if boat == 'left':
            new_state = (m_left - m, c_left - c, 'right', m_right + m, c_right + c)
        else:
            new_state = (m_left + m, c_left + c, 'left', m_right - m, c_right - c)

        if is_valid_state(new_state, missionaries, cannibals):
            next_states.append(new_state)

    return next_states

def solve_missionaries_cannibals(missionaries, cannibals):
    """Solve the Missionaries and Cannibals problem."""
    # Initial state: all missionaries and cannibals on the left side
    initial_state = (missionaries, cannibals, 'left', 0, 0)
    goal_state = (0, 0, 'right', missionaries, cannibals)

    # BFS setup
    queue = deque([(initial_state, [])])
    visited = set()

    while queue:
        current_state, path = queue.popleft()

        if current_state in visited:
            continue

        visited.add(current_state)
        path = path + [current_state]

        # Check if goal state is reached
        if current_state == goal_state:
            return path

        # Generate next valid states
        next_states = get_next_states(current_state, missionaries, cannibals)
        for state in next_states:
            queue.append((state, path))

    return None

if __name__ == "__main__":
    missionaries = int(input("Enter the number of missionaries: "))
    cannibals = int(input("Enter the number of cannibals: "))

    solution = solve_missionaries_cannibals(missionaries, cannibals)

    if solution:
        print("\nSolution found:")
        for step in solution:
            print(step)
    else:
        print("\nNo solution found.")
