import numpy as np
import time
from scipy.optimize import root


def newton_method(system, jacobian, x0, y0, tol, maxiter=100):
    """
    Решает систему нелинейных уравнений методом Ньютона

    Параметры:
    system - список функций системы
    jacobian - функция, возвращающая матрицу Якоби
    x0, y0 - начальные приближения
    tol - требуемая точность
    maxiter - максимальное число итераций

    Возвращает:
    solution - найденное решение
    iterations - количество итераций
    exec_time - время выполнения
    """
    start_time = time.time()
    x, y = x0, y0

    for iterations in range(1, maxiter + 1):
        # Вычисляем текущие значения функций
        F = np.array([system[0](x, y), system[1](x, y)])

        # Вычисляем матрицу Якоби
        J = jacobian(x, y)

        try:
            # Решаем систему линейных уравнений J*Δ = -F
            delta = np.linalg.solve(J, -F)
        except np.linalg.LinAlgError:
            print("Матрица Якоби вырождена. Метод Ньютона не может быть применен.")
            return None, iterations, time.time() - start_time

        # Обновляем решение
        x_new = x + delta[0]
        y_new = y + delta[1]

        # Проверяем условие остановки
        if np.linalg.norm([x_new - x, y_new - y]) < tol:
            exec_time = time.time() - start_time
            return (x_new, y_new), iterations, exec_time

        x, y = x_new, y_new

    exec_time = time.time() - start_time
    return (x, y), iterations, exec_time


# Определяем систему уравнений
system = [
    lambda x, y: np.sin(x + y) - 1.2 * x + 0.1,
    lambda x, y: x ** 2 + y ** 2 - 1
]


# Определяем матрицу Якоби
def jacobian(x, y):
    return [
        [np.cos(x + y) - 1.2, np.cos(x + y)],
        [2 * x, 2 * y]
    ]


# Начальные приближения
x0, y0 = 0.5, 0.5

# Точности
tolerances = [1e-3, 1e-4]

# Результаты
results = []

# Решение для каждой точности
for tol in tolerances:
    solution, iterations, exec_time = newton_method(system, jacobian, x0, y0, tol)
    if solution:
        x, y = solution

        results.append({
            'Точность': tol,
            'x': x,
            'y': y,
            'Итерации': iterations,
            'Время (сек)': exec_time,
        })

# Вывод результатов в виде таблицы
print("Результаты:")
print("=" * 80)
print(
    f"{'Точность':<10} | {'x':<15} | {'y':<15} | {'Итерации':<10} | {'Время (сек)':<12}")
print("-" * 80)
for res in results:
    print(f"{res['Точность']:<10.0e} | {res['x']:<15.8f} | {res['y']:<15.8f} | "
          f"{res['Итерации']:<10} | {res['Время (сек)']:<12.6f}")
