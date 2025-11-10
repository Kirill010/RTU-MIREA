import numpy as np
import time

# Параметры
N = 10
EPSILON = 1e-6
MAX_ITER = 100000


def analytical_solution(x):
    return 1.5 * x


def vector_norm(v):
    return np.linalg.norm(v)


def matrix_vector_mult(A, v):
    return A @ v


def dot_product(a, b):
    return np.dot(a, b)


# Простая итерация: u = f - A u  => решаем (I + A)u = f, но в форме u = f - A u
def simple_iteration(A, f, u, max_iter=MAX_ITER, tol=EPSILON):
    start_time = time.time()
    matrix_multiplies = 0
    u_new = np.copy(u)

    for k in range(max_iter):
        Au = matrix_vector_mult(A, u)
        matrix_multiplies += 1
        u_new = f - Au

        diff_norm = vector_norm(u_new - u)
        new_norm = vector_norm(u_new)
        if new_norm < 1e-15:
            new_norm = 1.0

        if diff_norm / new_norm < tol:
            u[:] = u_new
            return k + 1, time.time() - start_time, matrix_multiplies

        u[:] = u_new

        if vector_norm(u) > 1e10:
            print(f"Simple iteration diverges! Stopping at iteration {k + 1}")
            break

    return max_iter, time.time() - start_time, matrix_multiplies


# Градиентный спуск для (I + A)u = f
def gradient_descent(A, f, u, max_iter=MAX_ITER, tol=EPSILON):
    start_time = time.time()
    matrix_multiplies = 0
    I = np.eye(len(u))

    for k in range(max_iter):
        # r = (I + A)u - f
        Au = matrix_vector_mult(A, u)
        matrix_multiplies += 1
        r = u + Au - f

        # g = (I + A^T) r = r + A^T r; A симметричная → A^T = A
        Ar = matrix_vector_mult(A, r)
        matrix_multiplies += 1
        g = r + Ar

        numerator = dot_product(r, r)
        denominator = dot_product(g, g)

        if denominator < 1e-15:
            break

        alpha = numerator / denominator
        u -= alpha * g

        residual_norm = vector_norm(r)
        f_norm = vector_norm(f)
        if f_norm < 1e-15:
            f_norm = 1.0

        if residual_norm / f_norm < tol:
            return k + 1, time.time() - start_time, matrix_multiplies

    return max_iter, time.time() - start_time, matrix_multiplies


# BiCG
def bicg(A, f, u, max_iter=MAX_ITER, tol=EPSILON):
    start_time = time.time()
    matrix_multiplies = 0
    size = len(u)

    u[:] = 0.0
    r = f.copy()
    r_tilde = f.copy()
    p = r.copy()
    p_tilde = r_tilde.copy()

    rho_prev = 1.0

    for k in range(max_iter):
        rho = dot_product(r_tilde, r)
        if abs(rho) < 1e-15:
            print(f"BiCG: Breakdown at iteration {k} (rho=0)")
            break

        v = matrix_vector_mult(A, p)
        matrix_multiplies += 1
        alpha = rho / dot_product(r_tilde, v)

        u += alpha * p
        r -= alpha * v

        A_T_p_tilde = matrix_vector_mult(A, p_tilde)  # A^T = A
        matrix_multiplies += 1
        r_tilde -= alpha * A_T_p_tilde

        rho_new = dot_product(r_tilde, r)
        beta = rho_new / rho

        p = r + beta * p
        p_tilde = r_tilde + beta * p_tilde

        residual_norm = vector_norm(r)
        f_norm = vector_norm(f)
        if f_norm < 1e-15:
            f_norm = 1.0

        if residual_norm / f_norm < tol:
            return k + 1, time.time() - start_time, matrix_multiplies

        if residual_norm > 1e10 or np.isnan(residual_norm):
            print(f"BiCG diverges! Stopping at iteration {k + 1}")
            break

    return max_iter, time.time() - start_time, matrix_multiplies


# BiCGSTAB
def bicgstab(A, f, u, max_iter=MAX_ITER, tol=EPSILON):
    start_time = time.time()
    matrix_multiplies = 0
    size = len(u)

    u[:] = 0.0
    r = f.copy()
    r_tilde = r.copy()
    p = np.zeros_like(u)
    v = np.zeros_like(u)

    rho_prev = 1.0
    alpha = 1.0
    omega = 1.0

    for k in range(max_iter):
        rho = dot_product(r_tilde, r)
        if abs(rho) < 1e-15:
            print(f"BiCGSTAB: Breakdown at iteration {k} (rho=0)")
            break

        beta = (rho / rho_prev) * (alpha / omega)
        p = r + beta * (p - omega * v)

        v = matrix_vector_mult(A, p)
        matrix_multiplies += 1

        alpha = rho / dot_product(r_tilde, v)

        s = r - alpha * v
        t = matrix_vector_mult(A, s)
        matrix_multiplies += 1

        ts = dot_product(t, s)
        tt = dot_product(t, t)
        omega = ts / tt if abs(tt) > 1e-15 else 0.0

        u += alpha * p + omega * s
        r[:] = s - omega * t

        residual_norm = vector_norm(r)
        f_norm = vector_norm(f)
        if f_norm < 1e-15:
            f_norm = 1.0

        if residual_norm / f_norm < tol:
            return k + 1, time.time() - start_time, matrix_multiplies

        rho_prev = rho

        if residual_norm > 1e10 or np.isnan(residual_norm):
            print(f"BiCGSTAB diverges! Stopping at iteration {k + 1}")
            break

    return max_iter, time.time() - start_time, matrix_multiplies


def compute_error(u_num, u_analytical):
    diff = u_num - u_analytical
    num = np.dot(diff, diff)
    denom = np.dot(u_analytical, u_analytical)
    if denom < 1e-15:
        return np.sqrt(num)
    return np.sqrt(num / denom)


# Основная программа
def main():
    a, b = 0.0, 1.0
    lambda_val = 1.0
    h = (b - a) / N

    x = np.array([a + h * (i + 0.5) for i in range(N)])

    # Матрица интегрального оператора: A_ij = λ * h * x_i * x_j
    A_integral = np.zeros((N, N))
    for i in range(N):
        for j in range(N):
            A_integral[i, j] = lambda_val * h * x[i] * x[j]

    f = x.copy()  # f(x) = x
    u_analytical = analytical_solution(x)

    print(f"N = {N}")
    print(f"eps = {EPSILON}\n")

    # --- Simple Iteration ---
    u_si = np.zeros(N)
    iter_si, time_si, mult_si = simple_iteration(A_integral, f, u_si)
    error_si = compute_error(u_si, u_analytical)
    print("Simple Iteration Method:")
    print(f"  Iter: {iter_si}\n  Matrix mult: {mult_si}\n  Time: {time_si:.6f} sec\n  Error: {error_si:.6e}\n")

    # --- Gradient Descent ---
    u_gd = np.zeros(N)
    iter_gd, time_gd, mult_gd = gradient_descent(A_integral, f, u_gd)
    error_gd = compute_error(u_gd, u_analytical)
    print("Gradient Descent Method:")
    print(f"  Iter: {iter_gd}\n  Matrix mult: {mult_gd}\n  Time: {time_gd:.6f} sec\n  Error: {error_gd:.6e}\n")

    # --- BiCG ---
    u_bicg = np.zeros(N)
    iter_bicg, time_bicg, mult_bicg = bicg(A_integral, f, u_bicg)
    error_bicg = compute_error(u_bicg, u_analytical)
    print("BiConjugate Gradient Method (BiCG):")
    print(f"  Iter: {iter_bicg}\n  Matrix mult: {mult_bicg}\n  Time: {time_bicg:.6f} sec\n  Error: {error_bicg:.6e}\n")

    # --- BiCGSTAB ---
    u_bicgstab = np.zeros(N)
    iter_bicgstab, time_bicgstab, mult_bicgstab = bicgstab(A_integral, f, u_bicgstab)
    error_bicgstab = compute_error(u_bicgstab, u_analytical)
    print("Stabilized BiConjugate Gradient Method (BiCGSTAB):")
    print(
        f"  Iter: {iter_bicgstab}\n  Matrix mult: {mult_bicgstab}\n  Time: {time_bicgstab:.6f} sec\n  Error: {error_bicgstab:.6e}\n")

    # --- Сравнение ---
    print("Performance Comparison:")
    print(f"{'Method':<18} {'Iterations':<11} {'Matrix Mults':<13} {'Time (sec)':<12} {'Error'}")
    print(f"{'Simple Iter':<18} {iter_si:<11} {mult_si:<13} {time_si:<12.6f} {error_si:.10e}")
    print(f"{'Gradient Descent':<18} {iter_gd:<11} {mult_gd:<13} {time_gd:<12.6f} {error_gd:.10e}")
    print(f"{'BiCG':<18} {iter_bicg:<11} {mult_bicg:<13} {time_bicg:<12.6f} {error_bicg:.10e}")
    print(f"{'BiCGSTAB':<18} {iter_bicgstab:<11} {mult_bicgstab:<13} {time_bicgstab:<12.6f} {error_bicgstab:.10e}")


if __name__ == "__main__":
    main()
