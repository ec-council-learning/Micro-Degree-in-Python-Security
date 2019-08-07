# this is a single line comment
"""
This will be ignored
"""

# These variables control the web applications behaviour
a = 1 # this is the documentation for variable 'a' (useless)
b = 1 # This is a variable b
c = 1 # This is a variable c

"""This should be the summary

This should be a brief description.
THis is also part of the description....


What kind of variables it takes
What kind of return it produces...
"""

def multiply(baseSalary = None, raiseAmount = None):
    """This function supports the HR application related to the salary raise of employees.

    This function takes base salary, and a multiplicatant.
    It produces the raised salary for the employee.

    Arguments:
        baseSalary : int(the base salary)
        raiseAmount : float(the muliplier, or raise amount)

    Returns:
        double (the raised salary)
    """
    if not isinstance(baseSalary, int):
        raise ValueError("The baseSalary must be an integer!")
    if not isinstance(raiseAmount, float):
        raise ValueError("The raiseAmount must be a float value!")

    if baseSalary and raiseAmount:
        return round(baseSalary * raiseAmount,2)
    else:
        return None


class DemoClass(object):
    """This ais the documentation for the class.

    This class serves as an example for the documentation
    """
    def __init__(self, name = None):
        """This is the initialization of our class.

        The argument name needs to be passed as it will serve as a decorator, or property.
        """
        if not name:
            raise ValueError("This variable name needs to be defined.")
        self.__name = name
        

    @property
    def name(self):
        """This is the name property.

        This serves the encapsulation of the hiddent variable, to provide
        a controlled way to acces it!
        """
        return self.__name

