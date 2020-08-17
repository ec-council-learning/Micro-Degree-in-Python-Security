from math import pi


def arg_check(func):
    def wrapper(num):
        if type(num) != int:
            raise TypeError("Argument is not an integer")
        elif num <= 0:
            raise ValueError("Argument is not positive")
        else:
            return func(num)
    return wrapper


@arg_check
def circle_measures(radius):
    circum = 2 * pi * radius
    cir_area = pi * radius * radius
    diam = 2 * radius
    return diam, circum, cir_area


if __name__ == "__main__":
    diameter, circumference, area = circle_measures(6)
    print(f"The diameter is {diameter}.\nThe circumference is {circumference}.\nThe area is {area}")

