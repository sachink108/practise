import os
import sys
import threading

R = 12
C = 10
min_dist = sys.maxsize

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def isSafe(mat, visited, x ,y):
    if (mat[x][y] == 0 or visited[x][y]):
        return False
    return True

def isValid(x, y):
    if(x < R and y < C and x>=0 and y>=0):
        return True
    return False

def markUnsafeCells(mat):
    for i in range(0, R):
        for j in range(0, C):
            # if landmine is found
            if (mat[i][j] == 0):
                # mark all adjacent cells
                for k in range(0, 4):
                    if (isValid (i + rowNum[k], j+colNum[k])):
                        mat[i + rowNum[k]][j+colNum[k]] = -1

    print ("After marking unsafe")
    printMatrix(mat)
    # mark all found adjacent cells as unsafe
    for i in range(0, R):
        for j in range(0, C):
            if (mat[i][j] == -1):
                mat[i][j] = 0
    print ("After making all unsafe to 0")
    printMatrix(mat)

def printMatrix(mat):
    for row in mat:
        print (row)
    print()

def findShortestPathUtil(mat, visited, i, j, dist, path_len):
    global min_dist
    if (j == C-1):
        min_dist = min(dist, min_dist)
        return

    # if current path cost exceeds minimum so far
    if (dist > min_dist):
        return # dont try further

    visited[i][j] = path_len
    # recurse for all adjacent safe neighbors
    for k in range(0, 4):
        if (isValid(i + rowNum[k], j + colNum[k]) and isSafe(mat, visited, i + rowNum[k], j + colNum[k])):
            findShortestPathUtil (mat, visited, i + rowNum[k], j + colNum[k], dist + 1, path_len + 1)

    #backtrack
    visited[i][j] = 0

def findShortestPath(mat):
    global min_dist
    markUnsafeCells(mat)
    
    # start from the first column and take minimum
    for i in range(0, R):
        if (mat[i][0] == 1):
            # reset visited matrix
            visited = [[0]*(C) for i in range(0, R) ]
            findShortestPathUtil(mat, visited, i, 0, 0, 1)
            print ("Started at (%d, %d) : Min Dist = %d" % (i,0,min_dist))
            
            if (min_dist == C - 1):
                break;

    if (min_dist != sys.maxsize):
        print ("Length of the shortest path is ", min_dist)
    else:
        print ("Destination not reachable ", min_dist)


def main():
    mat = [ [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 0, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 0, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
            [ 1, 0, 1, 1, 1, 1, 1, 1, 0, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 0, 1, 1, 1, 1, 0, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 0, 1, 1, 1, 1, 1, 1 ]
        ];
 
    findShortestPath(mat);

main()
