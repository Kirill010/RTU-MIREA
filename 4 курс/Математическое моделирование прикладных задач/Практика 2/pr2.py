import numpy as np

# Константы
A_VAL, B_VAL = 0.0, 1.0
N = 3
LAMBDA_VAL = 1.0
EPSILON = 1e-6
MAX_ITER = 1000


def analytical_solution(x):
    return (-425.0 / 63.0) * x ** 3 + x ** 5 - 1.0


def kernel(x, t):
    return x ** 3 * (2 + t)


def f_function(x):
    return x ** 5 - 1.0


def main_numpy():
    h = (B_VAL - A_VAL) / N

    # Коллокационные точки
    x = np.array([i * h + h / 2.0 + A_VAL for i in range(N)])

    # Аналитическое решение
    y_analytical = analytical_solution(x)

    # Матрица системы и правая часть
    A = np.zeros((N, N))
    f = f_function(x)

    for i in range(N):
        for j in range(N):
            A[i, j] = -LAMBDA_VAL * h * kernel(x[i], x[j])
        A[i, i] += 1.0

    # Нормировка
    M = max(np.max(np.abs(A)), np.max(np.abs(f)))
    A_norm = A / M
    f_norm = f / M

    # Матрица B для итерационного метода
    B = -A_norm + np.eye(N)

    # Итерационный метод
    y_prev = f_norm.copy()

    for k in range(MAX_ITER):
        # Замена B @ y_prev на np.dot(B, y_prev)
        y_iter = np.dot(B, y_prev) + f_norm

        if np.linalg.norm(y_iter - y_prev) < EPSILON:
            break

        y_prev = y_iter.copy()

    # Вычисление ошибки
    error = np.sum(np.abs(y_analytical - y_iter)) / np.sum(np.abs(y_analytical))

    # Вывод результатов
    print("Интегральное уравнение: y(x) = ∫[0,1] (2+t)*x^3*y(t)dt + x^5 - 1")
    print("Точки коллокации (x):", [f"{val:.6f}" for val in x])
    print()

    print("Аналитическое решение y(x) = x^5 - 1:")
    for i in range(N):
        print(f"y({x[i]:.3f}) = {y_analytical[i]:.6f}")
    print()

    print("Численное решение:")
    for i in range(N):
        print(f"y_num({x[i]:.3f}) = {y_iter[i]:.6f}")
    print()

    print(f"Количество итераций: {k + 1}")
    print(f"Относительная ошибка: {error * 100:.6f}%")


if __name__ == "__main__":
    main_numpy()
