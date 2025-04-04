import numpy as np
import time


def gradient_method(system, x0, y0, tol, max_iter=10000, learning_rate=0.01):
    """
    Решает систему нелинейных уравнений градиентным методом

    Параметры:
    system - система уравнений (возвращает кортеж из двух значений)
    x0, y0 - начальные приближения
    tol - требуемая точность
    max_iter - максимальное количество итераций
    learning_rate - скорость обучения

    Возвращает:
    x, y - найденное решение
    iterations - количество итераций
    exec_time - время выполнения
    """
    start_time = time.time()
    x, y = x0, y0

    for iterations in range(1, max_iter + 1):
        # Вычисляем значения функций системы
        f1, f2 = system(x, y)

        # Вычисляем градиенты (производные по x и y)
        # Для f1 = sin(x+y) - 1.2x + 0.1
        df1_dx = np.cos(x + y) - 1.2
        df1_dy = np.cos(x + y)

        # Для f2 = x² + y² - 1
        df2_dx = 2 * x
        df2_dy = 2 * y

        # Вычисляем общий градиент (минимизируем сумму квадратов)
        grad_x = 2 * f1 * df1_dx + 2 * f2 * df2_dx
        grad_y = 2 * f1 * df1_dy + 2 * f2 * df2_dy

        # Обновляем решение
        x_new = x - learning_rate * grad_x
        y_new = y - learning_rate * grad_y

        # Проверяем условие остановки
        if np.abs(x_new - x) < tol and np.abs(y_new - y) < tol:
            exec_time = time.time() - start_time
            return x_new, y_new, iterations, exec_time

        x, y = x_new, y_new

    exec_time = time.time() - start_time
    return x, y, max_iter, exec_time


# Система уравнений для варианта 10
def system(x, y):
    return (
        np.sin(x + y) - 1.2 * x + 0.1,
        x ** 2 + y ** 2 - 1
    )


# Начальные приближения
x0, y0 = 0.5, 0.5

# Точности
tolerances = [1e-3, 1e-4]

# Результаты
results = []

# Решение для каждой точности
for tol in tolerances:
    x, y, iterations, exec_time = gradient_method(system, x0, y0, tol)
    results.append({
        'Точность': tol,
        'x': x,
        'y': y,
        'Итерации': iterations,
        'Время (сек)': exec_time
    })

# Вывод результатов в виде таблицы
print("Результаты:")
print("=" * 70)
print(f"{'Точность':<10} | {'x':<15} | {'y':<15} | {'Итерации':<10} | {'Время (сек)':<12}")
print("-" * 70)
for res in results:
    print(f"{res['Точность']:<10.0e} | {res['x']:<15.8f} | {res['y']:<15.8f} | "
          f"{res['Итерации']:<10} | {res['Время (сек)']:<12.6f}")

