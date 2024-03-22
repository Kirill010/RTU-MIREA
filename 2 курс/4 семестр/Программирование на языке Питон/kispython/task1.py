import math


def main(z):
    a = z ** 6 + 0.01
    b = ((z ** 3 + 0.01 + 11 * z) ** 5) / 4
    c = 56 * ((81 * z + 16 * z ** 2 + 34 * z ** 3) ** 3)
    d = 73 * ((math.cos((z ** 3) / 39)) ** 6)
    A = a / b
    C = c / d
    res = A - C
    return res


print(main(0.42))
print(main(0.15))
print(main(0.52))
print(main(0.74))
print(main(-0.87))
