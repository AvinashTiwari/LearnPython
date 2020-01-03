import threading
import time

def myfunction():
    print("A")
    time.sleep(3)
    print("B")

threads = []
for i in range(5):
    th = threading.Thread(target= myfunction)
    th.start()
    threads.append(th)

for th in threads:
    th.join()