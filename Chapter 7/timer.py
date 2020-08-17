import math
import time


def time_decorator(funct):
    def wrapper(*arg):
        result = funct(*arg)
        timer = time.perf_counter()
        # print(f"Timer: {timer}")
        return result, timer
    return wrapper


@time_decorator
def factorial_counter(x, y):
    fact = math.factorial(x)
    fact2 = math.factorial(y)
    # print(math.gcd(fact, fact2))
    return math.gcd(fact, fact2)


if __name__ == "__main__":
    for i in range(10):
        output = factorial_counter(10000, 10)
        print(f"GCD = {output[0]}, Timer = {output[1]}")
