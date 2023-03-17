# 15.1
import multiprocessing
import random
import time

def wait_random():
    wait_time = random.random()
    time.sleep(wait_time)
    print(time.time())

if __name__ == "__main__":
    for i in range(3):
        p = multiprocessing.Process(target=wait_random)
        p.start()

