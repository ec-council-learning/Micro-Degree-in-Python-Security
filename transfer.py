import pickle

class PickleClass(object):
    def __init__(self, name):
        self.__name = name

    @property
    def name(self):
        return self.__name


def sum(a,b):
    return a + b

my_list = [1,2.0,"3",4e5]

my_dictionary = {'a':1,'b':2}

a = PickleClass("ECCouncil")

with open("my_pickled.pickle","wb") as pickler:
    pickle.dump(PickleClass("ECCouncil"))

print(a)
