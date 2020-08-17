import multiprocessing
import time


def countdown(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)  # number of seconds
        print(f'{name} is counting down: {counter}...')
        counter -= 1

    print(f'{name} finished counting down')


if __name__ == '__main__':
    p1 = multiprocessing.Process(target=countdown, args=('Process Alice', 1))
    p2 = multiprocessing.Process(target=countdown, args=('Process Bob', 2))

    p1.start()
    p2.start()

    p1.join()
    p2.join()
