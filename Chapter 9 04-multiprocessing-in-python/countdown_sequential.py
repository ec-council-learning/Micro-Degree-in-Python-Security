import time


def countdown(name, delay):
    counter = 5

    while counter:
        time.sleep(delay)  # number of seconds
        print(f'{name} is counting down: {counter}...')
        counter -= 1

    print(f'{name} finished counting down')


if __name__ == '__main__':
    countdown('Alice', 1)
    countdown('Bob', 2)
