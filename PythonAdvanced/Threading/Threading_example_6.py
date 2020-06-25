import threading

class PrimeNumber(threading.Thread):
    def __init__(self, number):
        threading.Thread.__init__(self)
        self.Number = number

    def run(self):
        counter = 2
        while ((counter * counter) < self.Number):
            if self.Number % counter == 0:
                print("%d is no prime number, because %d = %d * %d" % (
                self.Number, self.Number, counter, self.Number / counter))
                return
            counter += 1
            print("%d is a prime number" % self.Number)

threads = []

while True:
    input1 = int(input("\nEnter number (0 to STOP): "))
    if input1 < 1:
        break

    thread = PrimeNumber(input1)
    threads += [thread] # Operator overloading in python
    thread.start()

# Even if an infinite loop breaks, below join() will ensure all started threads are executed
for x in threads:
    x.join()

print ("Main Thread completes!")