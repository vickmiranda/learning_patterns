import Queue
import threading
import urllib2
import time

# Notice that some url do not respond giving some errors and hanging the
# app when ran
hosts = ["http://apple.com", "http://averna.com", "http://google.com",
         "http://ibm.com", "http://yahoo.com", "http://linkedin.com"]
NUMBER_THREADS = 6

queue = Queue.Queue()


class ThreadUrl(threading.Thread):
    def __init__(self, queue):
        threading.Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            host = self.queue.get()
            url = urllib2.urlopen(host)
            print url.read(1024)
            # Signals to queue job is done
            self.queue.task_done()

def main():
    for i in range(NUMBER_THREADS):
        t = ThreadUrl(queue)
        t.setDaemon(True)
        t.start()
    print 'last for loop is non blocking'

    # populate queue with data
    for host in hosts:
        print 'current host: {}'.format(host)
        queue.put(host)

    queue.join()

if __name__ == '__main__':
    start_time = time.time()
    main()
    end_time = time.time()
    print 'elapsed time: %s' % (end_time - start_time)