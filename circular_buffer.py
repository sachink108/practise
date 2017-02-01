import os
import sys

class CircularBuffer:
    def __init__(self, size):
        self.size = size
        self.front = 0
        self.rear = 0
        self.list = [None] * size

    def get(self):
        ret = self.list[self.front]
        self.list[self.front] = None
        self.front += 1
        if (self.front == self.size):
            self.front = 0

        self.print()
        return ret

    def put(self, e):
        if (self.rear == self.size):
            self.rear = 0

        self.list[self.rear % self.size] = e
        self.rear += 1
        self.print()
        
    def print (self):
        print (self.list)


def main():
    c = CircularBuffer(5)
    c.put(1)
    c.put(2)
    c.put(3)
    c.put(4)
    c.put(5)
    print ("Getting")
    print(c.get())
    #c.put(6)
    #c.put(7)
    print (c.get())
    print (c.get())
    print(c.get())
    print(c.get())
    c.put(6)
    c.put(30)
    print(c.get())
    print(c.get())
   
if (__name__ == "__main__"):
    main()
