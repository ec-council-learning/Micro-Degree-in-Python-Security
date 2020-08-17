class CallTracer:
    def __init__(self, func):
        """# On @ decoration: save original func

        'calls' variable is a state retainer; it maintains knowledge of the number of function calls, since the function
        itself cannot. It is tied into the 'func' variable so each decorated function has its own state retention.
        """
        self.calls = 0  # Initial call to function is zero
        self.func = func  # Assign function name to instance

    def __call__(self, *args):
        """# On later calls: run original func"""
        self.calls += 1  # Increment function call amount
        print(f"Call number {self.calls} to function {self.func.__name__}")
        self.func(*args)  # Provide the arguments to the original function


@CallTracer
def spammer(*args):
    """Demonstrate summation or concatenation of any number of arguments.

    Only looking for integers and strings. All other types create an exception.
    'Null' values are provided as default values for 'x' to provide an initial value
    """
    try:
        for arg in args:
            if type(arg) == int:
                x = 0
            elif type(arg) == str:
                x = ""
            else:
                raise TypeError
            x += arg
            print(x, end="")
    except TypeError:
        print("Invalid type provided")
    print("\n")


if __name__ == "__main__":
    spammer(1, 2, 3)
    spammer("a", "b", "c")
    spammer(9, 8, 7, 6, 5)
    spammer(1.0, 2.0, 3.5)
