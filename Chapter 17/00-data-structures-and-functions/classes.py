#%% Class declaration.
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Point ({self.x}, {self.y})'

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def distance(self, p):
        diff = self - p
        dist = math.sqrt(diff.x ** 2 + diff.y ** 2)
        return dist


class EqualPoint(Point):
    def __init__(self, x):
        Point.__init__(self, x, x)


#%% Attributes of a class object can be accessed using a dot notation.
a = Point(1, 2)
b = Point(2, 3)
print(a.x)
print(b.y)
print()

#%% A class method can be called using a dot notation with the class object.
dist = a.distance(b)
print(dist)
print()

#%%
print(a)

c = a + b
print(c)
d = a - b
print(d)
print()

#%%
e = EqualPoint(3)
print(e)
print(e.distance(a))
