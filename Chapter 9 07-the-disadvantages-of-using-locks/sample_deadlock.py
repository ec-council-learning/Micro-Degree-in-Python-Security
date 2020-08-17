import time
import threading


lock_a = threading.Lock()
lock_b = threading.Lock()


def task1():
    print('Task 1 is starting...')

    print('Task 1 is waiting to acquire Lock A')
    with lock_a:
        print('Task 1 has acquired Lock A')

        print('Task 1 is doing some calculations')
        time.sleep(2)

        print('Task 1 is waiting to acquire Lock B')
        with lock_b:
            print('Task 1 has acquired Lock B')

            print('Task 1 is doing some calculations')
            time.sleep(2)

            print('Task 1 is releasing both locks')

def task2():
    print('Task 2 is starting...')

    print('Task 2 is waiting to acquire Lock B')
    with lock_b:
        print('Task 2 has acquired Lock B')

        print('Task 2 is doing some calculations')
        time.sleep(5)

        print('Task 2 is waiting to acquire Lock A')
        with lock_a:
            print('Task 2 has acquired Lock A')

            print('Task 2 is doing some calculations')
            time.sleep(5)

            print('Task 2 is releasing both locks')


if __name__ == '__main__':
    t1 = threading.Thread(target=task1)
    t2 = threading.Thread(target=task2)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

