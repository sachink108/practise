import os
import sys

def fib(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fib(n-1) + fib(n-2)    
    
def main():
    n = 9
    print ("Fib %d is %d" % (n, fib(n)))

if __name__ == '__main__':
    main()
