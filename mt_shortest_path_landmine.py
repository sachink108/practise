import os
import sys
import threading

R = 12
C = 10
min_dist = sys.maxsize

rowNum = [-1, 0, 0, 1]
colNum = [0, -1, 1, 0]

def printMatrix(mat):
    for row in mat:
        print (row)
    print()
    
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

def isSafe(mat,visited,x,y):
    ret = ''
    if (isValid(x,y)):
        if (mat[x][y] == 0 or visited[x][y]):
            if (visited[x][y]):
                ret = ("Visited", False)
            else:
                ret = ("Open", True)
        else:
            ret = ("Open", True)
    else:
        ret = ("Invalid", False)

    return ret

def isValid(x,y):
    if(x < R and y < C and x>=0 and y>=0):
        return True
    return False

class ThreadedFindShortestPathUtil(threading.Thread):
    def __init__(self, mat, i, j):
        threading.Thread.__init__(self)
        self.mat = mat
        self.visited = [[0]*(C) for i in range(0, R) ]
        self.i = i
        self.j = j
        self.dist = 0
        self.name = "Thread %d-%d" % (self.i, self.j)
        self.min_dist = sys.maxsize

    def run(self):
        print ("%s Starting Search\n" % self.name)
        self._search(self.i, self.j, self.dist)

    # here we are trying to find out all paths,
    # so we dont need a global minimum
    def _search(self, i, j, dist):
        print ("Started Search at %d, %d" %(i,j))
        if (j == C-1):
            self.min_dist = min(dist, self.min_dist)
            print ("%s Found Path of length %d" % (self.name,self.min_dist))
            return

        # this distance is within the same thread
        # why dont we find all paths within and thread
        # that will make it local min
        # and return to main thread
        # to calculate global min
        if (dist >= self.min_dist):
            print ("%s Current dist(%d) > min_dist (%d). Aborting." % (self.name,dist, self.min_dist))
            return
        
        self.visited[i][j] = 1
        # recurse for all adjacent safe neighbors
        for k in range(0, 4):
            (status, gonogo) = isSafe(self.mat, self.visited, i + rowNum[k], j + colNum[k])
            if (gonogo):
                print ("%s k = %d Moving to (%d,%d)" % (status, k, i + rowNum[k], j + colNum[k]))
                self._search(i + rowNum[k], j + colNum[k], dist + 1)
            else:
                print ("%s k = %d, i=%d, j=%d" % (status, k, i + rowNum[k], j + colNum[k]))

        #backtrack
        self.visited[i][j] = 0

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

    '''
    mat = [ [ 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 0, 1, 1 ],
            [ 1, 1, 1, 1, 0, 1 ],
            [ 1, 1, 1, 1, 1, 1 ],
            [ 1, 1, 1, 1, 1, 0 ],
        ];
    '''
    markUnsafeCells(mat)
    
    # start from the first column and take minimum
    for i in range(0, R):
         ts = ThreadedFindShortestPathUtil(mat, i, 0)
         ts.setDaemon(True)
         ts.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()

main()
