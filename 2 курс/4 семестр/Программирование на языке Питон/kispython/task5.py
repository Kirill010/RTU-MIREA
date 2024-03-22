import math


def main(z):
    res = 0
    n = len(z)
    for i in range(1, n + 1):
        res += ((z[n + 1 - (math.ceil((i) / 3) + 1)] ** 4) / 9)
    return 78 * res


arr = [0.95, 0.32, -0.84, -0.91, 0.06, 0.37, 0.2, -0.65]
print(main(arr))

arr1 = [-0.85, 0.24, -0.16, -0.36, -0.59, -0.35, 0.52, 0.91]
print(main(arr1))

arr2 = [-0.81, -0.79, 0.0, 0.1, -0.85, -0.48, 0.09, 0.94]
print(main(arr2))

arr3 = [0.23, 0.87, 0.98, -0.17, 0.09, 0.17, -0.02, -0.78]
print(main(arr3))

arr4 = [0.48, -0.43, -0.34, 0.38, 0.06, 0.79, -0.88, -0.45]
print(main(arr4))
