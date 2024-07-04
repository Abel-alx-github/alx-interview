#!/usr/bin/python3
"""N Queens"""
import sys


def print_board(board, n):
    """Print allocated positions to the queen"""
    box = []

    for x in range(n):
        for y in range(n):
            if y == board[x]:
                box.append([x, y])
    print(box)


def is_position_safe(board, x, y, r):
    """Checks if the position is safe for the queen"""
    return board[x] in (y, y - x + r, x - r + y)


def safe_positions(board, row, n):
    """Find all safe positions where the queen can be allocated"""
    if row == n:
        print_board(board, n)

    else:
        for y in range(n):
            allowed = True
            for x in range(row):
                if is_position_safe(board, x, y, row):
                    allowed = False
            if allowed:
                board[row] = y
                safe_positions(board, row + 1, n)


def create_board(size):
    """Generates the board"""
    return [0 * size for x in range(size)]


if len(sys.argv) != 2:
    print("Usage: nqueens N")
    exit(1)

try:
    n = int(sys.argv[1])
except BaseException:
    print("N must be a number")
    exit(1)

if (n < 4):
    print("N must be at least 4")
    exit(1)

board = create_board(int(n))
row = 0
safe_positions(board, row, int(n))
