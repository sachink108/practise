import os
import sys
from operator import itemgetter

a =  [[3,9,5,6,7],
      [6,5,4,3,2],
      [7,8,9,1,9],
      [1,2,3,4,5]
     ]
print (a)
#print (sorted(a, key = lambda x: x[2]))
print (sorted(a, key = itemgetter(1)))
