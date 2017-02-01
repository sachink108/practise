import os
import sys

def fib(n, lookup):
    if n == 0 or n == 1:
        lookup[n] = n

    if lookup[n] is None:
        lookup[n] = fib(n-1, lookup) + fib(n-2, lookup)

    return lookup[n]

def main():
    n = 9
    lookup = [None]* 100
    print ("Fib %d is %d" % (n, fib(n, lookup)))

if __name__ == '__main__':
    main()
