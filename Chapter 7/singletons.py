instances = {}


def singleton(class_name):  # On @ decoration
    def make_instance(*args, **kwargs):  # On instance creation
        if class_name not in instances:  # If class not already in dict
            instances[class_name] = class_name(*args, **kwargs)  # Add instance to dict
        return instances[class_name]

    return make_instance


@singleton  # Salary = singleton(Salary)
class Salary:  # Rebinds class Salary to make_instance()
    def __init__(self, name, hours, rate):  # make_instance() remembers Salary class
        self.name = name
        self.hours = hours
        self.rate = rate

    def pay(self):
        return self.hours * self.rate


@singleton  # Echo = singleton(Echo)
class Echo:  # Rebinds class Echo to make_instance()
    def __init__(self, val):  # make_instance() remembers Echo class
        self.attr = val


if __name__ == "__main__":
    bob = Salary('Bob', 40, 10)  # Really calls make_instance()
    print(f"{bob.name} earned {bob.pay()}")

    sue = Salary('Sue', 50, 20)  # Only one instance possible, so this creation does nothing
    print(f"{sue.name} earned {sue.pay()}")

    X = Echo(val=42)  # First instance
    Y = Echo(99)  # Only one instance possible, so this does creates nothing new
    print(X.attr, Y.attr)
