#What is a Thread?

#- A thread is a separate flow of execution.They allow you to have different parts of
# your process run concurrently which means that the process will have multiple things happening at one time.
#- These different parts are usually individual and have a separate unit of execution
# belonging to the same process. The process is nothing but a running program that has
# individual units that can be run concurrently.

# - Tasks that spend much of their time waiting for external events are generally
# good candidates for threading.

# -There are different types of threads:
# 1) Kernel thread
# 2) User thread
# 3) Combination of kernel and user thread

#Documentation: https://docs.python.org/3/library/threading.html#module-threading

#Python3 is backward compatible with the thread module, which exists in Python2.7.
# In Python3, it can be imported as _thread module(lower-level API) or threading module(high-Level API).

# There are two modules which support the usage of threads in Python3 −
#
# 1) _thread
# 2) threading

import logging
import threading
import time

def thread_function(name):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    logging.info("Thread %s: finishing", name)

if __name__ == "__main__":
    format = "%(asctime)s: %(message)s"
    logging.basicConfig(format=format, level=logging.INFO, datefmt="%H:%M:%S")
    logging.info("Main : before creating thread")
    x = threading.Thread(target=thread_function, args=(1,)) #args take in a tuple

    logging.info("Main    : before running thread")
    #start a separate thread
    x.start()
    #To wait until a daemon thread has completed its work, use the join() method
    logging.info("Main    : wait for the thread to finish")
    x.join()
    #By default, join() blocks indefinitely. It is also possible to pass a float value
    # representing the number of seconds to wait for the thread to become inactive.
    # If the thread does not complete within the timeout period, join() returns anyway.
    #x.join(0.1)
    logging.info("Main    : all done")
    # Check Thread class
    print(dir(threading.Thread))
