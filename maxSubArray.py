import os
import sys

def maxSubArraySum(a, size):
    max_so_far = 0
    max_ending_here = 0
    start_idx = 0
    end_idx = 0

    for i in range(0, size):
        max_ending_here = max_ending_here + a[i]
        if (max_ending_here < 0):
            max_ending_here = 0
            end_idx = i

        if (max_so_far < max_ending_here):
            max_so_far = max_ending_here
            start_idx = i

    print ("Start, End ", start_idx, end_idx)
    return max_so_far

a = [-2, -3, 4, -1, -2, 1, 5, -3]

print ("Max contiguous sum is ", maxSubArraySum(a, len(a)))


    

