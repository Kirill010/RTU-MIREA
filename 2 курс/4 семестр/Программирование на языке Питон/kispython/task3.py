import math


def main(n, p, m, a, x):
    res1 = 0
    for c in range(1, n + 1):
        res1 += 63 * ((c ** 3 + (70 * (p ** 2))) ** 5)

    res2 = 0
    for i in range(1, a + 1):
        for k in range(1, m + 1):
            res2 += ((93 * (math.sin(24 * x) ** 3)) + (85 * (math.log(k) ** 5)) + (((i + 0.01) ** 4) / 33))

    res = res1 + res2
    return res


print(main(7, 0.55, 5, 7, 0.68))
print(main(2, -0.94, 3, 8, -0.91))
print(main(7, 0.96, 5, 6, 0.17))
print(main(5, -0.17, 6, 8, 0.87))
print(main(3, -0.99, 7, 4, -0.61))
