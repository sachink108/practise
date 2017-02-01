import os
import sys
import threading
import time
import random

class ReturnValueFromThread(threading.Thread):
    def __init__(self, arr, idx):
        threading.Thread.__init__(self)
        self.idx = idx
        self.name="Thread %d" % self.idx
        self.arr = arr

    def run(self):
        t = random.choice([i for i in range(0, 5)])
        msg = "%s Sleeping for %d" % (self.name, t)
        print (msg)
        time.sleep(t)
        self.arr[self.idx] = msg

    def join(self):
        threading.Thread.join(self)
        print ("%s returning %d" %(self.name, self.idx))
        return self.name

def main():
    total = 10
    arr = [None] * total

    for i in range(0, 10):
        t = ReturnValueFromThread(arr, i)
        t.start()

    main_thread = threading.current_thread()
    for t in threading.enumerate():
        if t is main_thread:
            continue
        ret = t.join()
        print ("Main thread ret = %s " % ret)

    for i in range(0, total):
        print (arr[i])

main()
