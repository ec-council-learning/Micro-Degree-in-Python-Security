def decorator(arg1, arg2):
    def true_decorator(function):
        def wrapper(*args, **kwargs):
            print(f"This function has been decorated with arguments {arg1} and {arg2}")
            function(*args, **kwargs)
        return wrapper
    return true_decorator


@decorator("arg1", "arg2")
def print_args(*args):
    for arg in args:
        print(arg)


if __name__ == "__main__":
    print_args()
