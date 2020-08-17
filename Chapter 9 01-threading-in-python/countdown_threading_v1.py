import threading
import time


def countdown(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)  # number of seconds
        print(f'{name} is counting down: {counter}...')
        counter -= 1

    print(f'{name} finished counting down')


if __name__ == '__main__':
    t1 = threading.Thread(target=countdown, args=('Thread Alice', 1))
    t2 = threading.Thread(target=countdown, args=('Thread Bob', 2))

    t1.start()
    t2.start()

    t1.join()
    t2.join()
