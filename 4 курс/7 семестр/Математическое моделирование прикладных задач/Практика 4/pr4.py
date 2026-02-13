import numpy as np
import time

N = 3
EPSILON = 1e-6
MAX_ITER = 100000


def vector_norm(v):
    return np.linalg.norm(v)


def matrix_vector_mult(A, v):
    return A @ v


def dot_product(a, b):
    return np.dot(a, b)


def analytical_solution(x):
    return 1.5 * x


def simple_iteration(A, f, u):
    start_time = time.time()

    u_new = np.zeros_like(u)
    iterations = 0
    matrix_multiplies = 0

    for k in range(MAX_ITER):
        # Au = A * u
        Au = matrix_vector_mult(A, u)
        matrix_multiplies += 1

        # u_new = f - Au (т.к. u + Au = f => u = f - Au)
        u_new = f - Au

        # Проверка сходимости: ||u_new - u|| / ||u_new|| < ε
        diff_norm = vector_norm(u_new - u)
        new_norm = vector_norm(u_new)

        if new_norm < 1e-15:
            new_norm = 1.0

        if diff_norm / new_norm < EPSILON:
            iterations = k + 1
            u[:] = u_new
            break

        # Обновляем u
        u[:] = u_new
        iterations = k + 1

        # Защита от расходимости
        if vector_norm(u) > 1e10:
            print(f"Simple iteration diverges! Stopping at iteration {k + 1}")
            break

    time_spent = time.time() - start_time
    return iterations, time_spent, matrix_multiplies


def gradient_descent(A, f, u):
    start_time = time.time()

    size = len(u)
    iterations = 0
    matrix_multiplies = 0

    # Начальное приближение u0 = 0
    u.fill(0.0)

    for k in range(MAX_ITER):
        # r = (I + A)u - f
        Au = matrix_vector_mult(A, u)
        matrix_multiplies += 1
        r = u + Au - f

        # Градиент: g = (I + A^T)r = r + A^T r
        # Но так как A симметричная, то A^T = A
        Ar = matrix_vector_mult(A, r)
        matrix_multiplies += 1

        # Вычисляем шаг α
        numerator = dot_product(r, r)
        denominator = dot_product(r + Ar, r + Ar)

        if denominator < 1e-15:
            break

        alpha = numerator / denominator

        # Обновление: u_{k+1} = u_k - α * g
        u -= alpha * (r + Ar)

        # Проверка сходимости по невязке
        residual_norm = vector_norm(r)
        f_norm = vector_norm(f)

        if f_norm < 1e-15:
            f_norm = 1.0

        if residual_norm / f_norm < EPSILON:
            iterations = k + 1
            break

        iterations = k + 1

    time_spent = time.time() - start_time
    return iterations, time_spent, matrix_multiplies


def two_step_gradient_descent(A, f, u):
    start_time = time.time()

    size = len(u)
    iterations = 0
    matrix_multiplies = 0

    # Начальное приближение u0 = 0
    u.fill(0.0)
    u_prev = np.zeros_like(u)

    # Первая итерация - обычный градиентный спуск
    if MAX_ITER > 0:
        # r0 = (I + A)u0 - f = -f (т.к. u0 = 0)
        r = -f.copy()

        # A * r
        Ar = matrix_vector_mult(A, r)
        matrix_multiplies += 1

        # Вычисляем шаг α
        numerator = dot_product(r, r)
        denominator = dot_product(r + Ar, r + Ar)

        if denominator > 1e-15:
            alpha = numerator / denominator
            u[:] = u_prev - alpha * (r + Ar)

        iterations = 1

    # Сохраняем предыдущие значения
    u_prev = u.copy()
    r_prev = r.copy()

    # Основной цикл итераций
    for k in range(1, MAX_ITER):
        # Вычисляем невязку r_k
        Au = matrix_vector_mult(A, u)
        matrix_multiplies += 1
        r = u + Au - f

        # A * r_k
        Ar = matrix_vector_mult(A, r)
        matrix_multiplies += 1

        # Вычисляем оптимальные параметры
        rr = dot_product(r, r)
        r_prev_r_prev = dot_product(r_prev, r_prev)

        # Простой двухшаговый метод с рестартом
        beta = rr / r_prev_r_prev if (rr > 1e-15 and r_prev_r_prev > 1e-15) else 0.0

        # Ограничиваем beta для стабильности
        if beta > 1.0:
            beta = 0.0

        # Обновление: u_{k+1} = u_k - α*(r + Ar) + β*(u_k - u_{k-1})
        numerator = dot_product(r, r)
        denominator = dot_product(r + Ar, r + Ar)

        if denominator > 1e-15:
            alpha = numerator / denominator
            u_new = u - alpha * (r + Ar) + beta * (u - u_prev)
            u_prev = u.copy()
            u[:] = u_new

        # Обновляем предыдущую невязку
        r_prev = r.copy()

        # Проверка сходимости по невязке
        residual_norm = vector_norm(r)
        f_norm = vector_norm(f)

        if f_norm < 1e-15:
            f_norm = 1.0

        if residual_norm / f_norm < EPSILON:
            iterations = k + 1
            break

        # Защита от расходимости
        if residual_norm > 1e10 or np.isnan(residual_norm):
            print(f"Two-step method diverges! Stopping at iteration {k + 1}")
            break

        iterations = k + 1

    time_spent = time.time() - start_time
    return iterations, time_spent, matrix_multiplies


def compute_error(u_num, u_analytical):
    return vector_norm(u_num - u_analytical) / vector_norm(u_analytical)


def main():
    a, b = 0.0, 1.0
    lambda_val = 1.0
    h = (b - a) / N

    # точки коллокации
    x = np.array([a + h * (i + 0.5) for i in range(N)])

    # Матрица A для интегрального оператора (без единичной матрицы!)
    A_integral = np.zeros((N, N))
    f = np.zeros(N)

    for i in range(N):
        for j in range(N):
            # Интегральный оператор: A_ij = λ * h * K(x_i, x_j) = 1.0 * h * x[i] * x[j]
            A_integral[i, j] = lambda_val * h * x[i] * x[j]
        f[i] = x[i]  # правая часть f(x) = x

    u_analytical = analytical_solution(x)

    print(f"N = {N}")
    print(f"eps = {EPSILON:e}\n")

    # Простая итерация
    u_si = np.zeros(N)
    iter_si, time_si, mult_si = simple_iteration(A_integral, f, u_si)
    error_si = compute_error(u_si, u_analytical)

    print("Simple Iteration Method:")
    print(f"  Iter: {iter_si}")
    print(f"  Matrix mult: {mult_si}")
    print(f"  Time: {time_si:.6f} sec")
    print(f"  Error: {error_si:.6e}\n")

    # Градиентный спуск
    u_gd = np.zeros(N)
    iter_gd, time_gd, mult_gd = gradient_descent(A_integral, f, u_gd)
    error_gd = compute_error(u_gd, u_analytical)

    print("Gradient Descent Method:")
    print(f"  Iter: {iter_gd}")
    print(f"  Matrix mult: {mult_gd}")
    print(f"  Time: {time_gd:.6f} sec")
    print(f"  Error: {error_gd:.6e}\n")

    # Двухшаговый метод градиентного спуска
    u_ts = np.zeros(N)
    iter_ts, time_ts, mult_ts = two_step_gradient_descent(A_integral, f, u_ts)
    error_ts = compute_error(u_ts, u_analytical)

    print("Two-Step Gradient Descent:")
    print(f"  Iter: {iter_ts}")
    print(f"  Matrix mult: {mult_ts}")
    print(f"  Time: {time_ts:.6f} sec")
    print(f"  Error: {error_ts:.6e}\n")

    print("Performance Comparison:")
    print("Method           Iterations  Matrix Mults  Time (sec)  Error")
    print(f"Simple Iter      {iter_si:<11} {mult_si:<13} {time_si:<11.6f} {error_si:.10e}")
    print(f"Gradient Descent {iter_gd:<11} {mult_gd:<13} {time_gd:<11.6f} {error_gd:.10e}")
    print(f"Two-Step GD      {iter_ts:<11} {mult_ts:<13} {time_ts:<11.6f} {error_ts:.10e}")


if __name__ == "__main__":
    main()
