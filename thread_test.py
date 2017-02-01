import os
import sys
import threading
import time

exitFlag = 0
class ThreadedSearch (threading.Thread):
    def __init__(self, threadID, name, counter):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name
        self.counter = counter
        
    def run(self):
        print ("Starting " + self.name)
        print_time(self.name, self.counter, 5)
        print ("Exiting " + self.name)

def print_time(threadName, delay, counter):
    while counter:
        if exitFlag:
            threadName.exit()
        time.sleep(delay)
        print ("%s: %s" % (threadName, time.ctime(time.time())))
        counter -= 1


t1 = ThreadedSearch(1, "thread-1", 2)
t2 = ThreadedSearch(2, "thread-2", 3)
t1.start()
t2.start()

main_thread = threading.current_thread()
for t in threading.enumerate():
    if t is main_thread:
        continue
    print ("Waiting to complete")
    t.join()
print ("Program Terminated")
