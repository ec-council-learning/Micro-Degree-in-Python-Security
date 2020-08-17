
class TestClass(object):
    ClassVariable = 101
    def __init__(self, name):
        self.__name = name
        self.__hidden = "You can not touch this!"

    @property
    def name(self):
        return self.__name
    
    @property
    def hidden(self):
        return self.__hidden

    @hidden.setter 
    def hidden(self, value):
        self.__hidden = value

    @classmethod
    def classer(cls):
        return "This is the class method, and it's cool!"
    
    @staticmethod
    def staticer():
        return "This is a static method!"
    
    def __str__(self):
        return f"This is a class called: {self.__class__.__name__}"

    def __repr__(self):
        return f"This is from the repr of class called: {self.__class__.__name__}"
    
    def __format__(self):
        return f"This is from the __format__ function of the class called: {self.__class__.__name__}"

A = TestClass("ECCouncil")

print(A.name)
print(A.hidden)
A.hidden = "A new value"
print(A.hidden)
print(TestClass.classer())
print(A.staticer())
print(A)
print(repr(A))

print("{a}".format(a=A))

