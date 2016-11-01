import time
import threading
import Queue

myqueue = Queue.Queue()


class CountStuff(threading.Thread):
    def __init__(self, start, end, queue):
        self.num = start
        self.end = end
        self.queue = queue
        threading.Thread.__init__(self)

    def run(self):
        while True:
            if self.num != self.end:
                self.num += 1
                self.queue.put(self.num)
                time.sleep(1)
            else:
                break

myThread = CountStuff(1, 5, myqueue)
myThread.start()

while True:
    if not myqueue.empty():
        val = myqueue.get()
        print 'outputing {}'.format(val)
        time.sleep(2)
    else:
        break


