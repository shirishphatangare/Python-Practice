#example of multi threading with locking to fetch several URLs and save the results in a file:

import threading as thread
import urllib.request as urllib2

# This function fetch the data from a URL
def getData(url):
    try:
        f = urllib2.urlopen(url)
        data = f.read()
        f.close()
    except urllib2.URLError:
        data = "Not found. URLError"
    return data

# This one tries to save the data from a URL into a file.
# it is a common function to shared resource (the file) and
# therefore requires a lock
def fetchURL(url, filename, lock):
    data = getData(url)
    print("%s was requested and returned" % url)
    lock.acquire()
    try:
        f = open(filename, "a")
        f.write("Data from %s fetched\n" % url) # Not writing all data to file here
        f.close()
    finally:
        lock.release()

lock = thread.Lock()

thread1 = thread.Thread(target=fetchURL, args=("http://www.yahoo.fr","resources//test.txt",lock))
thread2 = thread.Thread(target=fetchURL, args=("http://www.lemonde.fr","resources//test.txt",lock))
thread3 = thread.Thread(target=fetchURL, args=("http://www.youtube.fr","resources//test.txt",lock))

thread1.start()
thread2.start()
thread3.start()
