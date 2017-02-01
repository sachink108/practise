import os
import sys

a = list("abcdaf")
b = list("acbcf")

al = len(a)
bl = len(b)
matrix = [[None] * (bl+1) for i in range(0, al+1)]

for i in range(al+1):
    for j in range(bl+1):
        if (i ==0 or j == 0):
            matrix[i][j] = 0
        elif (a[i-1] == b[j-1]):
            matrix[i][j] = matrix[i-1][j-1]+1
        else:
            matrix[i][j] = max(matrix[i-1][j], matrix[i][j-1])

for row in matrix:
    print(row)
    
print (matrix[al][bl])
