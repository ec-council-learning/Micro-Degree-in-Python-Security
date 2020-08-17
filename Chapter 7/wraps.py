from functools import wraps


def this_decorator(funct):
    @wraps(funct)
    def wrapper(*args, **kwargs):
        print("This is the decorated function")
        return funct(*args, **kwargs)
    return wrapper


@this_decorator
def call_me():
    """Docstring for call_me()"""
    print("This is the example function")


def that_decorator(funct):
    def wrapper(*args, **kwargs):
        print("This is the decorated function")
        return funct(*args, **kwargs)
    return wrapper


@that_decorator
def call_you():
    """Docstring for call_you()"""
    print("This is the example function")


if __name__ == "__main__":
    call_me()
    print(call_me.__name__)  # Would have been "wrapper" w/o functools
    print(call_me.__doc__)  # Would have been lost w/o functools

    call_you()
    print(call_you.__name__)
    print(call_you.__doc__)

