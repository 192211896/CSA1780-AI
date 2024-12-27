import heapq

class PuzzleState:
    def __init__(self, board, moves=0, previous=None):
        self.board = board
        self.moves = moves
        self.previous = previous

    def __lt__(self, other):
        return (self.moves + self.heuristic()) < (other.moves + other.heuristic())

    def heuristic(self):
        """Calculates the Manhattan distance heuristic."""
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.board[i][j]
                if value != 0:  # Ignore the blank space
                    target_x = (value - 1) // 3
                    target_y = (value - 1) % 3
                    distance += abs(target_x - i) + abs(target_y - j)
        return distance

    def is_goal(self, goal):
        return self.board == goal

    def get_neighbors(self):
        """Generates neighboring states by sliding tiles."""
        neighbors = []
        x, y = [(i, row.index(0)) for i, row in enumerate(self.board) if 0 in row][0]  # Locate the blank space
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < 3 and 0 <= ny < 3:
                new_board = [row[:] for row in self.board]
                new_board[x][y], new_board[nx][ny] = new_board[nx][ny], new_board[x][y]
                neighbors.append(PuzzleState(new_board, self.moves + 1, self))
        return neighbors


def print_board(board):
    for row in board:
        print(' '.join(map(str, row)))
    print()


def solve_puzzle(start, goal):
    open_set = []
    heapq.heappush(open_set, PuzzleState(start))
    visited = set()

    while open_set:
        current = heapq.heappop(open_set)

        if current.is_goal(goal):
            return current

        visited.add(tuple(tuple(row) for row in current.board))

        for neighbor in current.get_neighbors():
            neighbor_tuple = tuple(tuple(row) for row in neighbor.board)
            if neighbor_tuple not in visited:
                heapq.heappush(open_set, neighbor)

    return None


def get_input():
    print("Enter the puzzle state row by row, with spaces between numbers (use 0 for the blank space):")
    board = []
    for _ in range(3):
        row = list(map(int, input().split()))
        board.append(row)
    return board


def main():
    print("Define the initial state:")
    start = get_input()

    print("Define the goal state:")
    goal = get_input()

    print("Solving the puzzle...")
    solution = solve_puzzle(start, goal)

    if solution:
        steps = []
        while solution:
            steps.append(solution.board)
            solution = solution.previous
        steps.reverse()

        print(f"Solution found in {len(steps) - 1} moves:")
        for step in steps:
            print_board(step)
    else:
        print("No solution found.")


if __name__ == "__main__":
    main()
