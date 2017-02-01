import os
import sys
import threading
import time

class ThreadedSearch(threading.Thread):
    def __init__(self,matrix, word, row, col, index, n):
        threading.Thread.__init__(self)
        self.matrix = matrix
        self.word = word
        self.row = row
        self.col = col
        self.index = index
        self.n = n
        self.name = "Thread %d-%d" % (self.row, self.col)
        self.solution = [[0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0],
                         [0,0,0,0,0]
                        ]

    def run(self):
        print ("%s Started Search" % (self.name))
        ret = self._search(self.row, self.col, self.index)
        print ("%s Ended Search" % (self.name))
        if (ret is True):
            sol_str = "\n%s Found the Word\n" % (self.name)
            for i in range(0, len(self.matrix)):
                for j in range(0, len(self.matrix[0])):
                    sol_str += "%s " % str(self.solution[i][j])
                sol_str += "\n";
            print (sol_str);
                        
    def _search(self, row, col, index):
        if (self.solution[row][col] != 0 or self.word[index] != self.matrix[row][col]):
            return False

        if (index == len(self.word) - 1):
            self.solution[row][col] = self.word[index]
            return True

        self.solution[row][col] = self.word[index]

        # go down
        if (row + 1 < self.n and self._search(row+1, col, index+1)):
            return True
    
        # go up
        if (row-1 >=0 and self._search(row-1, col, index+1)):
            return True

        # go right
        if (col+1 < self.n and self._search(row, col+1, index+1)):
            return True

        # go left
        if (col-1 >=0 and self._search(row, col-1, index+1)):
            return True

        # go down right
        if (row+1 < self.n and col+1 < self.n and self._search(row+1, col+1, index+1)):
            return True

        # go down left
        if (row+1 < self.n and col-1 >=0 and self._search(row+1, col-1, index+1)):
            return True

        # go up right
        if (row-1 >= 0 and col+1 < self.n and self._search(row-1, col+1, index+1)):
            return True

        # go up left
        if (row-1 >= 0 and col-1 >=0 and self._search(row-1, col-1, index+1)):
            return True

        # backtrack, if we reached here after all the above
        # ifs then we did not find the word, hence reset the status
        self.solution[row][col] = 0
        return False

def main():
    rows = 5;
    cols = 5;
    matrix = [ [ 'z', 'h', 'o', 'r', 'i' ],
               [ 'o', 'i', 'w', 'z', 'z' ],
               [ 'n', 'w', 'r', 'o', 'o' ],
               [ 'u', 'o', 'p', 'o', 'n' ], 
               [ 'a', 'b', 'n', 'o', 'h' ] 
             ]

    target_word = "horizon"
    n = 5
    for i in range(0, rows):
        for j in range(0, cols):
            ts = ThreadedSearch(matrix, target_word, i, j, 0, n)
            ts.setDaemon(True)
            ts.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        t.join()
    print ("Search Program Ended")
main()
