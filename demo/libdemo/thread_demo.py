from threading import Thread
import threading


class PrintThread(Thread):
    def run(self):
        for i in range(1, 10):
            print(f"Child : {i}")


print("In Main Thread!!")
pt = PrintThread()
pt.start()


def print_numbers():
    for n in range(1, 20):
        print(f"Child 2 : {n}")


t = Thread(target=print_numbers)
t.start()

for i in range(1, 20):
    print(f"Main : {i}")
