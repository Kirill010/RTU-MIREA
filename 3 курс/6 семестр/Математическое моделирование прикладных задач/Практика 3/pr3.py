import math


def calculate_1(M, S, v, alpha):
    g = 10
    rho = 0.5

    if alpha is not None:
        alpha = math.radians(alpha)

    if S is None:
        S = (M * g) / (2 * rho * (v ** 2) * (alpha ** 2))
        return S

    elif M is None:
        M = (S * 2 * rho * (v ** 2) * (alpha ** 2)) / g
        return M

    elif v is None:
        v = math.sqrt((M * g) / (2 * rho * S * (alpha ** 2)))
        return v

    elif alpha is None:
        alpha = math.sqrt((M * g) / (2 * rho * S * (v ** 2)))
        return math.degrees(alpha)


def calculate_2(S, v, alpha):
    rho = 0.5
    u = 3000

    alpha = math.radians(alpha)

    mu = (2 * rho * S * (alpha ** 3) * v ** 2) / u
    return mu


print("Введите три известных параметра. 4-й параметр нужно найти.")
M = input("Масса самолета (кг): ")
S = input("Площадь крыла (м^2): ")
v = input("Скорость (м/с): ")
alpha = input("Угол отклонения (в градусах): ")

M = float(M) if M else None
S = float(S) if S else None
v = float(v) if v else None
alpha = float(alpha) if alpha else None

missing_param = calculate_1(M, S, v, alpha)

if M is None:
    M = missing_param
    print("Вычисленная масса самолета: ", round(M), "кг")
elif S is None:
    S = missing_param
    print("Вычисленная площадь крыла: ", round(S), "м²")
elif v is None:
    v = missing_param
    print("Вычисленная скорость: ", round(v), "м/с")
elif alpha is None:
    alpha = missing_param
    print("Вычисленный угол отклонения: ", round(alpha), "°")

mu = calculate_2(S, v, alpha)
print("Масса вылетающих газов: ", round(mu), "кг")
