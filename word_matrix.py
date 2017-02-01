import os
import sys

solution = [[0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0],
            [0,0,0,0,0]
           ]
path = 1

def searchWord(matrix, word):
    n = 5
    for i in range(0, rows):
        for j in range(0, cols):
            if (search(matrix, word, i, j, 0, n)):
                return True

def search(matrix, word, row, col, index, n):
    global path
    # first condition is that this is already searched and marked
    # by whom? someone else? what if there are overlapping paths?
    if (solution[row][col] != 0 or word[index] != matrix[row][col]):
        return False

    if (index == len(word) - 1):
        solution[row][col] = path
        path = path + 1
        return True

    solution[row][col] = path
    path = path + 1

    # go down
    if (row + 1 < n and search(matrix, word, row+1, col, index+1, n)):
        return True
    
    # go up
    if (row-1 >=0 and search(matrix, word, row-1, col, index+1, n)):
        return True

    # go right
    if (col+1 < n and search(matrix, word, row, col+1, index+1, n)):
        return True

    # go left
    if (col-1 >=0 and search(matrix, word, row, col-1, index+1, n)):
        return True

    # go down right
    if (row+1 < n and col+1 < n and search(matrix, word, row+1, col+1, index+1, n)):
        return True

    # go down left
    if (row+1 < n and col-1 >=0 and search(matrix, word, row+1, col-1, index+1, n)):
        return True

    # go up right
    if (row-1 >= 0 and col+1 < n and search(matrix, word, row-1, col+1, index+1, n)):
        return True

    # go up left
    if (row-1 >= 0 and col-1 >=0 and search(matrix, word, row-1, col-1, index+1, n)):
        return True

    # backtrack
    solution[row][col] = 0
    path = path - 1

    return False

rows = 5;
cols = 5;
matrix = [ [ 'p', 'o', 'r', 'i', 'h' ],
           [ 'h', 'h', 'w', 'z', 'o' ],
	   [ 'r', 'w', 'o', 'o', 'r' ],
	   [ 'u', 'o', 'p', 'n', 'i' ], 
	   [ 'a', 'b', 'n', 'o', 'z' ] 
        ]


def main():
    global solution
    target_word = "horizon"
    searchWord(matrix, target_word)

    for i in range(0, rows):
        for j in range(0, cols):
            print(solution[i][j], end='')
        print()
main()
