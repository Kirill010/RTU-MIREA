import math


def main(Om: set):
    a = set([i for i in Om if i >= -99 and i <= -2])
    qtty = set([(2 * j - 9 * j) for j in a if j <= -3 and j >= -57])
    tmp = set([(i ** 3 + abs(j)) for i in Om for j in a if i > j])
    ov = qtty | tmp
    count = len(ov)
    r = 0
    for m in tmp:
        for k in qtty:
            r += (math.ceil(m / 2) + abs(k))
    res = r + count
    return res


num = {-92, -20, 13, -82, -48, 16, 84, -9, -37, 63}
num1 = {98, 67, 41, 10, 81, 21, -42, -72, -38, 63}
print(main(num))
print(main(num1))
