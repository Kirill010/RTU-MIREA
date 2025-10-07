import numpy as np
import time

N = 10
EPSILON = 1e-6
MAX_ITER = 10000


def allocate_matrix(rows, cols):
    """Выделение памяти под матрицу"""
    return np.zeros((rows, cols))


def allocate_vector(size):
    """Выделение памяти под вектор"""
    return np.zeros(size)


def vector_norm(v):
    """Норма вектора"""
    return np.linalg.norm(v)


def matrix_vector_mult(A, v):
    """Умножение матрицы на вектор"""
    return A @ v


def analytical_solution(x):
    """Аналитическое решение"""
    return 1.5 * x


def simple_iteration(A, f, u):
    """Метод простой итерации"""
    start_time = time.time()

    max_val = max(np.max(np.abs(A)), np.max(np.abs(f)))

    if max_val == 0.0:
        print("Matrix and vector are zero — trivial solution.")
        return u, 0, 0, 0.0

    # Нормировка
    A_norm = A / max_val
    f_norm = f / max_val

    # B = I - A_norm
    B = np.eye(len(A)) - A_norm

    u_current = u.copy()
    iterations = 0
    matrix_multiplies = 0

    for k in range(MAX_ITER):
        temp = matrix_vector_mult(B, u_current)
        matrix_multiplies += 1

        u_new = temp + f_norm

        norm_diff = vector_norm(u_new - u_current)
        norm_f = vector_norm(f_norm)

        if ((norm_f < 1e-14 and norm_diff < EPSILON) or
                (norm_f >= 1e-14 and norm_diff / norm_f < EPSILON)):
            iterations = k + 1
            u_current = u_new
            break

        u_current = u_new
        iterations = k + 1

    time_spent = time.time() - start_time
    return u_current, iterations, matrix_multiplies, time_spent


def gradient_descent(A, f, u):
    """Метод градиентного спуска"""
    start_time = time.time()

    u_current = u.copy()
    iterations = 0
    matrix_multiplies = 0

    for k in range(MAX_ITER):
        # r = A*u - f
        r = matrix_vector_mult(A, u_current) - f
        matrix_multiplies += 1

        # g = A.T @ r
        g = matrix_vector_mult(A.T, r)
        matrix_multiplies += 1

        # Ag = A @ g
        Ag = matrix_vector_mult(A, g)
        matrix_multiplies += 1

        # alpha = (g,g)/(Ag,Ag)
        num = np.dot(g, g)
        den = np.dot(Ag, Ag)

        if den < 1e-15:
            break

        alpha = num / den

        u_new = u_current - alpha * g

        norm_diff = vector_norm(u_new - u_current)
        norm_f = vector_norm(f)

        if ((norm_f < 1e-14 and norm_diff < EPSILON) or
                (norm_f >= 1e-14 and norm_diff / norm_f < EPSILON)):
            iterations = k + 1
            u_current = u_new
            break

        u_current = u_new
        iterations = k + 1

    time_spent = time.time() - start_time
    return u_current, iterations, matrix_multiplies, time_spent


def compute_error(u_num, u_analytical):
    """Вычисление ошибки"""
    num = np.sum(np.abs(u_num - u_analytical))
    denom = np.sum(np.abs(u_analytical))

    if denom < 1e-15:
        return num
    return num / denom


def main():
    a = 0.0
    b = 1.0
    lambda_val = 1.0
    h = (b - a) / N

    # Создание сетки
    x = np.array([a + h * (i + 0.5) for i in range(N)])

    # Создание матрицы A и вектора f
    A = allocate_matrix(N, N)
    f = allocate_vector(N)

    for i in range(N):
        for j in range(N):
            A[i, j] = lambda_val * h * x[i] * x[j]
        A[i, i] += 1.0
        f[i] = x[i]

    # Аналитическое решение
    u_analytical = analytical_solution(x)

    # Метод простой итерации
    u_si_initial = allocate_vector(N)
    u_si, iter_si, mult_si, time_si = simple_iteration(A, f, u_si_initial)
    error_si = compute_error(u_si, u_analytical)

    # Метод градиентного спуска
    u_gd_initial = allocate_vector(N)
    u_gd, iter_gd, mult_gd, time_gd = gradient_descent(A, f, u_gd_initial)
    error_gd = compute_error(u_gd, u_analytical)

    print(f"N = {N}")
    print(f"eps = {EPSILON:e}\n")

    print("Simple Iteration Method:")
    print(f"  Iter: {iter_si}")
    print(f"  Matrix mult: {mult_si}")
    print(f"  Time: {time_si:.6f} sec")
    print(f"  Error: {error_si:.6e}\n")

    print("Gradient Descent Method:")
    print(f"  Iter: {iter_gd}")
    print(f"  Matrix mult: {mult_gd}")
    print(f"  Time: {time_gd:.6f} sec")
    print(f"  Error: {error_gd:.6e}\n")

    print("Performance Ratios (Grad_des / Simp_iter):")
    if iter_si > 0 and mult_si > 0 and time_si > 0:
        print(f"  Iter ratio: {iter_gd / iter_si:.2f}")
        print(f"  Mult ratio: {mult_gd / mult_si:.2f}")
        print(f"  Time ratio: {time_gd / time_si:.2f}")


if __name__ == "__main__":
    main()
