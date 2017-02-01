import os
import sys

N = 4

def printMatrix():
    for row in matrix:
        print (row)
        
def isSafe(board, row, col):
    # check on left side
    for i in range(0, col):
        if (board[row][i]):
            return False

    # check upper diagonal on left side
    i = row
    j = col
    while (i >= 0 and j >= 0):
        if (board[i][j]):
            return False
        i -= 1
        j -= 1

    # check lower left diagonal
    i,j = row,col
    while (i < N and j >= 0):
        if (board[i][j]):
            return False
        i += 1
        j -= 1

    return True
        
def solveNQUtil(board, col):
    if (col >= N):
        return True

    for i in range(0, N):
        if (isSafe(board, i, col)):
            board[i][col] = 1

            if (solveNQUtil(board, col+1)):
                return True

            # if we came here that means solveNQUtil above failed
            # so we backtrack
            board[i][col] = 0

    return False
        
def solveNQ():
    board = [[0] * N for i in range(0,N)]
    if (solveNQUtil(board, 0) == false):
        print ("Solution Does not exist")
    else:
        printMatrix(board)

def main():
    solveNQ()

if __name__ == "__main__":
    main()
