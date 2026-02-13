import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
import time

x_center = 0.0
y_center = 0.0
H = 10.0
N_values = [10, 20, 30, 40]
EPSILON = 1e-6
MAX_ITER = 100000


def kernel(x, y):
    # Ядро (левая часть)
    diff = abs(x - y)
    distance = np.sqrt(diff[0] ** 2 + diff[1] ** 2)
    if distance < 1e-12:
        return 0.0
    return 1.0 / (4.0 * np.pi * distance)


def f_func(x):
    # Правая часть f(x) = sin(x1) + cos(x2)
    return np.sin(x[0]) + np.cos(x[1])


def create_grid(N):
    # Создает сетку для квадратной области [-H/2, H/2] x [-H/2, H/2]
    h = H / N

    # Центры ячеек
    x_coords = np.linspace(x_center - H / 2 + h / 2, x_center + H / 2 - h / 2, N)
    y_coords = np.linspace(y_center - H / 2 + h / 2, y_center + H / 2 - h / 2, N)

    # Создаем матрицы координат
    X, Y = np.meshgrid(x_coords, y_coords)

    # Преобразуем в плоские массивы для удобства
    points = np.array([[X.flatten()[i], Y.flatten()[i]] for i in range(N * N)])
    cell_size = h

    return points, cell_size, X, Y


def build_matrix_A(N):
    """Строит матрицу A = I + K*h**2 для метода коллокаций"""
    points, h, _, _ = create_grid(N)
    n_points = len(points)
    h_squared = h ** 2

    A = np.eye(n_points)

    for i in range(n_points):
        for j in range(n_points):
            if i != j:
                A[i, j] = kernel(points[i], points[j]) * h_squared

    return A, points, h


def build_vector_f(points):
    n_points = len(points)
    f = np.zeros(n_points)
    for i in range(n_points):
        f[i] = f_func(points[i])
    return f


def vector_norm(v):
    return np.linalg.norm(v)


def dot_product(a, b):
    return np.dot(a, b)


# 1. Метод простой итерации
def simple_iteration(A, f, u0=None, max_iter=MAX_ITER, tol=EPSILON):
    n = len(f)
    if u0 is None:
        u = np.zeros(n)
    else:
        u = u0.copy()

    start_time = time.time()
    matrix_multiplies = 0

    for k in range(max_iter):
        Au = A @ u
        matrix_multiplies += 1
        u_new = f - Au + u

        residual = A @ u_new - f
        matrix_multiplies += 1
        residual_norm = vector_norm(residual)

        if residual_norm < tol:
            return u_new, k + 1, time.time() - start_time, matrix_multiplies

        u = u_new

        if residual_norm > 1e10:
            print(f"Simple iteration diverges at iteration {k}")
            break

    return u, max_iter, time.time() - start_time, matrix_multiplies


# 2. Метод градиентного спуска
def gradient_descent(A, f, u0=None, max_iter=MAX_ITER, tol=EPSILON):
    n = len(f)
    if u0 is None:
        u = np.zeros(n)
    else:
        u = u0.copy()

    start_time = time.time()
    matrix_multiplies = 0

    for k in range(max_iter):
        # Вычисление невязки r = A*u - f
        r = A @ u - f
        matrix_multiplies += 1

        # Вычисление направления p = A^T * r
        p = A.T @ r
        matrix_multiplies += 1

        # Оптимальный шаг alpha = (r·r) / (p·r)
        numerator = dot_product(r, r)
        denominator = dot_product(p, r)

        if abs(denominator) < 1e-15:
            break

        alpha = numerator / denominator

        # Обновление решения
        u = u - alpha * r

        # Проверка сходимости
        residual_norm = vector_norm(r)
        if residual_norm < tol:
            return u, k + 1, time.time() - start_time, matrix_multiplies

    return u, max_iter, time.time() - start_time, matrix_multiplies


# 3. Двухшаговый метод градиентного спуска
def two_step_gradient_descent(A, f, u0=None, max_iter=MAX_ITER, tol=EPSILON):
    n = len(f)
    if u0 is None:
        u = np.zeros(n)
    else:
        u = u0.copy()

    start_time = time.time()
    matrix_multiplies = 0

    # Первый шаг
    r = A @ u - f
    matrix_multiplies += 1
    p = A.T @ r
    matrix_multiplies += 1

    for k in range(max_iter):
        # Сохраняем старые значения
        r_old = r.copy()
        p_old = p.copy()

        # Вычисляем шаг alpha
        numerator = dot_product(r_old, r_old)
        denominator = dot_product(p_old, r_old)

        if abs(denominator) < 1e-15:
            break

        alpha = numerator / denominator

        # Обновляем решение
        u = u - alpha * r_old

        # Вычисляем новую невязку
        r = A @ u - f
        matrix_multiplies += 1

        # Вычисляем beta для двухшагового метода
        beta = dot_product(r, r) / numerator

        # Обновляем направление
        p = A.T @ r + beta * p_old
        matrix_multiplies += 1

        # Проверка сходимости
        residual_norm = vector_norm(r)
        if residual_norm < tol:
            return u, k + 1, time.time() - start_time, matrix_multiplies

    return u, max_iter, time.time() - start_time, matrix_multiplies


# 4. Стабилизированный метод бисопряженных градиентов
def bicgstab(A, f, u0=None, max_iter=MAX_ITER, tol=EPSILON):
    n = len(f)
    if u0 is None:
        u = np.zeros(n)
    else:
        u = u0.copy()

    start_time = time.time()
    matrix_multiplies = 0

    r = f - A @ u
    matrix_multiplies += 1
    r0_hat = r.copy()

    rho = 1.0
    alpha = 1.0
    omega = 1.0

    v = np.zeros(n)
    p = np.zeros(n)

    for k in range(max_iter):
        rho_old = rho
        rho = dot_product(r0_hat, r)

        if abs(rho) < 1e-15:
            break

        if k == 0:
            p = r.copy()
        else:
            beta = (rho / rho_old) * (alpha / omega)
            p = r + beta * (p - omega * v)

        v = A @ p
        matrix_multiplies += 1

        alpha = rho / dot_product(r0_hat, v)
        s = r - alpha * v

        t = A @ s
        matrix_multiplies += 1

        omega = dot_product(t, s) / dot_product(t, t)

        u = u + alpha * p + omega * s
        r = s - omega * t

        # Проверка сходимости
        residual_norm = vector_norm(r)
        if residual_norm < tol:
            return u, k + 1, time.time() - start_time, matrix_multiplies

        # Защита от расходимости
        if residual_norm > 1e10 or np.isnan(residual_norm):
            print(f"BiCGSTAB diverges at iteration {k}")
            break

    return u, max_iter, time.time() - start_time, matrix_multiplies


def plot_solution(u, X, Y, N, method_name):
    """Строит тепловую карту решения и сохраняет в файл"""
    U_matrix = u.reshape((N, N))

    plt.figure(figsize=(10, 8))

    # Тепловая карта
    im = plt.imshow(U_matrix, extent=[-H / 2, H / 2, -H / 2, H / 2],
                    origin='lower', cmap=cm.viridis, aspect='auto')
    plt.colorbar(im, label='Решение U(x,y)')

    plt.title(f'Решение интегрального уравнения\n{method_name}, N={N}')
    plt.xlabel('x1')
    plt.ylabel('x2')
    plt.grid(True, alpha=0.3)

    # Сохраняем график
    plt.show()


def plot_all_methods_comparison(solutions, X, Y, N):
    """Сравнительная визуализация всех методов для одного N"""
    methods = list(solutions.keys())

    fig, axes = plt.subplots(2, 2, figsize=(15, 12))
    axes = axes.flatten()

    for idx, method_name in enumerate(methods):
        if method_name in solutions:
            U_matrix = solutions[method_name].reshape((N, N))

            ax = axes[idx]
            im = ax.imshow(U_matrix, extent=[-H / 2, H / 2, -H / 2, H / 2],
                           origin='lower', cmap=cm.viridis, aspect='auto')
            ax.set_title(f'{method_name}\nN={N}')
            ax.set_xlabel('x1')
            ax.set_ylabel('x2')
            ax.grid(True, alpha=0.3)

            # Добавляем цветовую шкалу
            plt.colorbar(im, ax=ax, label='U(x,y)')

    plt.suptitle(f'Сравнение решений всеми методами для N={N}', fontsize=16)
    plt.tight_layout()
    plt.show()


def main():
    results_table = []

    for N in N_values:
        print(f"Расчет для N = {N}")

        # 1. Построение сетки и матрицы
        A, points, h = build_matrix_A(N)
        f = build_vector_f(points)
        n_total = N * N

        print(f"   Размерность задачи: {n_total} x {n_total}")
        print(f"   Размер ячейки: h = {h:.4f}")
        print(f"   h**2 = {h ** 2:.6f}")

        # 2. Решение разными методами
        methods = [
            ("Метод простой итерации", simple_iteration),
            ("Градиентный спуск", gradient_descent),
            ("Двухшаговый градиентный спуск", two_step_gradient_descent),
            ("BiCGSTAB", bicgstab)
        ]

        solutions = {}
        u0 = np.zeros(n_total)  # начальное приближение

        for method_name, method_func in methods:
            print(f"\n2. Решение методом: {method_name}")

            u_solution, iterations, elapsed_time, matrix_mults = method_func(A, f, u0, tol=EPSILON)

            # Сохраняем решение
            solutions[method_name] = u_solution

            # Вычисляем невязку
            residual = A @ u_solution - f
            residual_norm = vector_norm(residual)

            print(f"   Итераций: {iterations}")
            print(f"   Умножений матрицы на вектор: {matrix_mults}")
            print(f"   Время: {elapsed_time:.4f} сек")
            print(f"   Норма невязки: {residual_norm:.6e}")

            # Добавляем в таблицу результатов
            results_table.append({
                'N': N,
                'Method': method_name,
                'Iterations': iterations,
                'MatrixMultiplies': matrix_mults,
                'Time': elapsed_time,
                'Residual': residual_norm
            })

        # 3. Визуализация для КАЖДОГО метода
        _, _, X, Y = create_grid(N)

        # Визуализация каждого метода отдельно
        for method_name in solutions.keys():
            plot_solution(solutions[method_name], X, Y, N, method_name)

        # Сравнительная визуализация всех методов
        print("\n   Сравнительная визуализация всех методов...")
        filename_comparison = plot_all_methods_comparison(solutions, X, Y, N)
        print(f"   Сравнительный график сохранен: {filename_comparison}")

    # 4. Сводная таблица результатов
    print(f"{'N':<5} {'Метод':<30} {'Итерации':<10} {'Умножения':<12} {'Время (с)':<12} {'Невязка':<15}")

    for result in results_table:
        print(f"{result['N']:<5} {result['Method']:<30} {result['Iterations']:<10} "
              f"{result['MatrixMultiplies']:<12} {result['Time']:<12.4f} {result['Residual']:<15.2e}")

    # Группируем результаты по N
    for N in N_values:
        N_results = [r for r in results_table if r['N'] == N]
        print(f"\nN = {N}:")
        for res in N_results:
            print(f"  {res['Method']}: {res['Iterations']} итераций, "
                  f"невязка = {res['Residual']:.2e}, время = {res['Time']:.3f} сек")

    # 6. Сравнение методов по производительности

    methods_list = ["Метод простой итерации", "Градиентный спуск",
                    "Двухшаговый градиентный спуск", "BiCGSTAB"]

    for method in methods_list:
        method_results = [r for r in results_table if r['Method'] == method]
        avg_iter = np.mean([r['Iterations'] for r in method_results])
        avg_time = np.mean([r['Time'] for r in method_results])
        avg_residual = np.mean([r['Residual'] for r in method_results])

        print(f"\n{method}:")
        print(f"  Среднее число итераций: {avg_iter:.1f}")
        print(f"  Среднее время: {avg_time:.4f} сек")
        print(f"  Средняя невязка: {avg_residual:.2e}")


if __name__ == "__main__":
    results = main()
