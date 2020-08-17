import time
import random
import threading


COUNTER = 0


def update():
    global COUNTER

    read_value = COUNTER  # reading in the shared resource
    time.sleep(random.randint(0, 1))  # simulating heavy calculations
    COUNTER = read_value + 1


if __name__ == '__main__':
    threads = [threading.Thread(target=update) for _ in range(20)]

    for t in threads:
        t.start()

    for t in threads:
        t.join()

    print(f'Final counter value: {COUNTER}')
