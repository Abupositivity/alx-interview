#!/usr/bin/python3
""" N queens puzzle"""
import sys


def print_solution(board):
    """Prints the board configuration as a list of positions."""
    solution = []
    for row in range(len(board)):
        solution.append([row, board[row]])
    print(solution)


def is_safe(board, row, col):
    """Checks if a queen can be placed on the board at position (row, col)."""
    for r in range(row):
        c = board[r]
        if c == col or abs(c - col) == abs(r - row):
            return False
    return True


def solve_n_queens(board, row, n):
    """Uses backtracking to find all solutions for the N Queens problem."""
    if row == n:
        print_solution(board)
        return
    for col in range(n):
        if is_safe(board, row, col):
            board[row] = col
            solve_n_queens(board, row + 1, n)
            board[row] = -1  # Backtrack


def main():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    board = [-1] * n  # Initialize the board with -1 (no queens placed)
    solve_n_queens(board, 0, n)


if __name__ == "__main__":
    main()
