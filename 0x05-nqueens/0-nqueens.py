#!/usr/bin/env py
from sys import argv


def solveNQueens(size: int):
    """solves the nqueens problem

    Args:
        n (int): _description_

    Returns:
        List[List[int]]: _description_
    """
    column_set = set()
    posDiag = set()
    negDiag = set()
    results = []
    board = [[0] * size for i in range(size)]

    def backtrack(row):
        """the backtrack recursive function

        Args:
            row (_type_): _description_
        """
        if row == size:
            results.append(
                [[idx, row.index(1)] for idx, row in enumerate(board)]
            )
            return

        for column in range(size):
            if column in column_set or \
                (row+column) in posDiag or\
                    (row-column) in negDiag:
                continue

            column_set.add(column)
            posDiag.add(row+column)
            negDiag.add(row-column)
            board[row][column] = 1

            backtrack(row+1)

            column_set.remove(column)
            posDiag.remove(row+column)
            negDiag.remove(row-column)
            board[row][column] = 0

    backtrack(0)
    return results


if len(argv) != 2:
    print("Usage: nqueens N")
    exit(1)
size = argv[1]
try:
    size = int(size)
    if not isinstance(size, int):
        raise ValueError
except ValueError:
    print("N must be a number")
    exit(1)
if size < 4:
    print("N must be at least 4")
    exit(1)
else:
    for item in solveNQueens(size):
        print(item)
