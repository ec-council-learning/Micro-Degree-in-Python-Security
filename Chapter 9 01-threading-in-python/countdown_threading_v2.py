import threading
import time


class CountThread(threading.Thread):
    def __init__(self, name, delay):
        threading.Thread.__init__(self)
        self.name = 'Thread ' + name
        self.delay = delay

    def run(self):
        print(f'{self.name} starting...')
        countdown(self.name, self.delay)
        print(f'{self.name} finished')


def countdown(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)  # number of seconds
        print(f'{name} is counting down: {counter}...')
        counter -= 1

    print(f'{name} finished counting down')


if __name__ == '__main__':
    thread1 = CountThread('Alice', 1)
    thread2 = CountThread('Bob', 2)

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()
