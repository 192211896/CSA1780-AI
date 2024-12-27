def print_solution(solution):
    """Prints the chessboard for a given solution."""
    for row in solution:
        print(" ".join("Q" if col == row else "." for col in range(len(solution))))
    print("\n")


def is_safe(board, row, col):
    """Checks if placing a queen at (row, col) is safe."""
    for i in range(row):
        if (
            board[i] == col or  # Same column
            board[i] - i == col - row or  # Same diagonal (top-left to bottom-right)
            board[i] + i == col + row  # Same diagonal (top-right to bottom-left)
        ):
            return False
    return True


def solve_n_queens(n, row=0, board=None, solutions=None):
    """Recursively solves the N-Queens problem."""
    if solutions is None:
        solutions = []
    if board is None:
        board = [-1] * n

    if row == n:
        solutions.append(board[:])
        return solutions

    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(n, row + 1, board, solutions)
            board[row] = -1  # Backtrack

    return solutions


def main():
    """Main function to solve the N-Queens problem."""
    try:
        n = int(input("Enter the size of the chessboard (e.g., 8 for 8-queens): "))
        if n < 1:
            print("The size of the chessboard must be at least 1.")
            return

        solutions = solve_n_queens(n)
        print(f"Found {len(solutions)} solutions for {n}-Queens.")
        for idx, solution in enumerate(solutions, start=1):
            print(f"\nSolution {idx}: {solution}")
            print_solution(solution)

    except ValueError:
        print("Please enter a valid integer.")


if __name__ == "__main__":
    main()
