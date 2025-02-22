import math
a = float(input())
b = float(input())
c = float(input())
D = b * b - 4 * a * c
if (a == 0):
    if (b == 0):
        if (c == 0):
            print("X - любое число")
        else:
            print("Нет решений")
    else:
        X = -c / b
        print(X)
else:
    if (D >= 0):
        x1 = ((-b - math.sqrt(D)) / (2 * a))
        x2 = ((-b + math.sqrt(D)) / (2 * a))
        print(x1, x2)
    else:
        print("Решение находится в области комплексных чисел")
