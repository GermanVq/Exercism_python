
def square(number):
    if number not in range(1, 65):
        raise ValueError("RangeError")
    return 2 ** (number - 1)


def total():
   return sum([square(x) for x in range(1,65)])