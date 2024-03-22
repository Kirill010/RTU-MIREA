import math


def main(x):
    if x < 135:
        a = 63 + (16 * (math.tan(72 - (x ** 2)) ** 4)) + (61 * (x ** 3))
        return a
    elif 135 <= x < 208:
        b = (69 * (x - 36) ** 2) + 2
        return b
    elif x >= 208:
        c = ((1 - (x ** 3) - (45 * x)) / 43) - 1
        return c


print(main(235))
print(main(191))
print(main(90))
print(main(122))
print(main(247))
