#!/usr/bin/python3
"""
N-Queens Problem Solver

This program solves the N queens puzzle N×N chessboard.
"""


import sys


def is_safe(board, row, col):
    """
    Check if it's safe to place a queen in given row and column chessboard.

    Args:
        board (list): The N×N chessboard represented as a 2D list.
        row (int): The row where you want to place the queen.
        col (int): The column where you want to place the queen.

    Returns:
        bool: True if it's safe to place a queen, False otherwise.
    """

    # Check if there is a queen in the same column
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, len(board))):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(N):
    """
    Solve the N queens problem for the given N and print the solutions.

    Args:
        N (int): The size of the chessboard and the number of queens to place.
    """

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]

    def solve(row):
        if row == N:
            for i in range(N):
                for j in range(N):
                    if board[i][j] == 1:
                        print([i, j])
            print()
            return

        for col in range(N):
            if is_safe(board, row, col):
                board[row][col] = 1
                solve(row + 1)
                board[row][col] = 0

    solve(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    solve_nqueens(N)
