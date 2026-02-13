import numpy as np
import matplotlib.pyplot as plt

# Данные из условия
spectrum = np.array([
    3 - 1.1j,
    5 - 1j,
    4 + 4j,
    2 + 3j,
    1 + 1j,
    6 + 1j
])

A = np.diag(spectrum)  # диагональная матрица
f = np.full(len(spectrum), 1 + 2j)  # правая часть
x0 = np.zeros_like(f)  # начальное приближение

print("Матрица A (диагональная):")
print(A)
print("\nПравая часть f:")
print(f)
print("\nСпектр оператора:")
for i, lam in enumerate(spectrum):
    print(f"λ_{i + 1} = {lam:.3f}")


def circle_from_2(p1, p2):
    """Окружность по двум точкам (диаметр)"""
    c = (p1 + p2) / 2
    r = abs(p1 - c)
    return c, r


def circle_from_3(p1, p2, p3):
    """Окружность по трем точкам"""
    # Решаем систему: |z - c| = R для трёх точек
    z = np.array([p1, p2, p3], dtype=complex)
    x = z.real
    y = z.imag

    # Система уравнений для центра окружности
    A_mat = np.array([
        [2 * (x[1] - x[0]), 2 * (y[1] - y[0])],
        [2 * (x[2] - x[0]), 2 * (y[2] - y[0])]
    ])
    b = np.array([
        x[1] ** 2 + y[1] ** 2 - x[0] ** 2 - y[0] ** 2,
        x[2] ** 2 + y[2] ** 2 - x[0] ** 2 - y[0] ** 2
    ])

    try:
        cx, cy = np.linalg.solve(A_mat, b)
        c = cx + 1j * cy
        r = abs(p1 - c)
        return c, r
    except np.linalg.LinAlgError:
        return None, None


def covers_all(c, r, pts, eps=1e-9):
    """Проверяет, покрывает ли окружность все точки"""
    return np.all(np.abs(np.array(pts) - c) <= r + eps)


def find_minimal_circle(points):
    """Находит минимальную окружность, покрывающую все точки"""
    pts = list(points)
    n = len(pts)
    best_c, best_r = None, float('inf')

    # Проверяем все пары точек (окружность с диаметром через эти точки)
    for i in range(n):
        for j in range(i + 1, n):
            c, r = circle_from_2(pts[i], pts[j])
            if r < best_r and covers_all(c, r, pts):
                best_c, best_r = c, r

    # Проверяем все тройки точек
    for i in range(n):
        for j in range(i + 1, n):
            for k in range(j + 1, n):
                c, r = circle_from_3(pts[i], pts[j], pts[k])
                if c is not None and r < best_r and covers_all(c, r, pts):
                    best_c, best_r = c, r

    # Fallback: если не нашли, берем окружность с центром в центре масс
    if best_c is None:
        c = np.mean(pts)
        r = np.max(np.abs(np.array(pts) - c))
        return c, r

    return best_c, best_r


def calculate_mu0_R_formula(lambda1, lambda2):
    """Вычисляет μ₀ и R по заданной формуле"""
    lambda1_conj = np.conj(lambda1)
    lambda2_conj = np.conj(lambda2)

    # Вычисление μ₀
    numerator_mu = 1j * np.imag(lambda1 * lambda2_conj) * (lambda2 - lambda1)
    denominator_mu = 2 * (np.abs(lambda1 * lambda2_conj) + np.real(lambda1 * lambda2_conj))
    mu0 = (lambda1 + lambda2) / 2 + numerator_mu / denominator_mu

    # Вычисление R
    numerator_R = np.abs(lambda1 - lambda2) ** 2 * np.abs(lambda1_conj * lambda2)
    denominator_R = 2 * (np.abs(lambda1_conj * lambda2) + np.real(lambda1_conj * lambda2))
    R = np.sqrt(numerator_R / denominator_R)

    return mu0, R


def find_optimal_mu_R(spectrum):
    """Находит оптимальные μ и R перебором всех пар точек"""
    n = len(spectrum)
    best_mu, best_R = None, float('inf')
    best_pair = None

    for i in range(n):
        for j in range(i + 1, n):
            mu_candidate, R_candidate = calculate_mu0_R_formula(spectrum[i], spectrum[j])

            # Проверяем, покрывает ли окружность все точки
            if covers_all(mu_candidate, R_candidate, spectrum) and R_candidate < best_R:
                best_mu, best_R = mu_candidate, R_candidate
                best_pair = (i, j)

    # Если не нашли пару, используем минимальную окружность
    if best_mu is None:
        return find_minimal_circle(spectrum)

    print(f"Оптимальная пара: λ_{best_pair[0] + 1} и λ_{best_pair[1] + 1}")
    return best_mu, best_R


# Находим оптимальные μ и R
mu, R = find_optimal_mu_R(spectrum)
print(f"\nНайдено μ = {mu:.6f}")
print(f"Найдено R = {R:.6f}")


# Обобщенный метод простой итерации
def generalized_iteration_method(A, f, mu, x0, tol=1e-8, max_iter=1000):
    """
    x_{k+1} = x_k - (1/μ)*(A*x_k - f)
    """
    n = len(f)
    x = x0.copy()

    print(f"\nЗапуск обобщенного метода простой итерации:")
    print(f"μ = {mu:.6f}")
    print(f"Допуск: {tol}")
    print(f"Максимальное число итераций: {max_iter}")

    for it in range(max_iter):
        residual = A @ x - f

        # Итерационная формула: x_{k+1} = x_k - (1/μ)*(A*x_k - f)
        x_new = x - (1 / mu) * residual

        # Критерий остановки
        norm_residual = np.linalg.norm(residual)
        norm_diff = np.linalg.norm(x_new - x)

        if it % 100 == 0:
            print(f"Итерация {it:4d}: невязка = {norm_residual:.2e}")

        if norm_residual < tol:
            print(f"\nСходимость достигнута за {it + 1} итераций")
            print(f"Финальная невязка: {norm_residual:.2e}")
            return x_new, it + 1, True

        x = x_new

    print(f"\nДостигнуто максимальное число итераций ({max_iter})")
    final_residual = np.linalg.norm(A @ x - f)
    print(f"Финальная невязка: {final_residual:.2e}")
    return x, max_iter, False


# Решаем СЛАУ
solution, iterations, converged = generalized_iteration_method(A, f, mu, x0)

# Проверка решения
print(f"\nПроверка решения:")
residual = A @ solution - f
residual_norm = np.linalg.norm(residual)
print(f"Норма невязки A*x - f: {residual_norm:.2e}")

# Сравнение с точным решением (для диагональной матрицы)
exact_solution = f / spectrum
print(f"\nТочное решение (для диагональной матрицы):")
error = np.linalg.norm(solution - exact_solution)
print(f"Ошибка по сравнению с точным решением: {error:.2e}")


# Визуализация
def visualize_spectrum(spectrum, mu, R):
    plt.figure(figsize=(10, 8))

    # Спектр
    plt.scatter(spectrum.real, spectrum.imag,
                c='black',
                s=150,
                linewidth=1.5,
                zorder=10,
                marker='o')

    angles = np.angle(spectrum - mu)
    order = np.argsort(angles)
    ordered_pts = spectrum[order]
    xs = np.append(ordered_pts.real, ordered_pts.real[0])
    ys = np.append(ordered_pts.imag, ordered_pts.imag[0])
    plt.plot(xs, ys, color='black', linestyle='--', linewidth=1.2,
             alpha=0.8, zorder=3, label='Многоугольник спектра')

    theta = np.linspace(0, 2 * np.pi, 400)
    circle_x = mu.real + R * np.cos(theta)
    circle_y = mu.imag + R * np.sin(theta)
    plt.plot(circle_x, circle_y,
             color='blue',
             linewidth=3,
             linestyle='-',
             alpha=0.9,
             label=f'Оптим. окружность ($R = {R:.3f}$)')

    # Центр
    plt.scatter([mu.real], [mu.imag],
                c='red',
                s=220,
                edgecolors='black',
                linewidth=0.8,
                zorder=15,
                label=f'Оптим. центр $\\mu = {mu:.3f}$')
    plt.text(mu.real + 0.2, mu.imag + 0.2,
             '$\\mu$',
             fontsize=16,
             fontweight='bold',
             color='tab:red',
             ha='left', va='bottom')

    # Оси и сетка
    plt.axhline(0, color='gray', linewidth=0.8, zorder=1)
    plt.axvline(0, color='gray', linewidth=0.8, zorder=1)
    plt.grid(True, which='both',
             linestyle='--',
             linewidth=0.7,
             alpha=0.7,
             color='gray')

    # Пропорции и границы
    plt.gca().set_aspect('equal')
    margin = R * 0.2
    plt.xlim(mu.real - R - margin, mu.real + R + margin)
    plt.ylim(mu.imag - R - margin, mu.imag + R + margin)

    # Оформление
    plt.xlabel('Re', fontsize=14)
    plt.ylabel('Im', fontsize=14)
    plt.title('Обобщенный метод простой итерации', fontsize=16, pad=20)

    # Легенда
    plt.legend(loc='upper left',
               fontsize=8,
               frameon=True,
               fancybox=True,
               shadow=True,
               framealpha=0.95,
               edgecolor='darkgray')

    plt.tight_layout()
    plt.show()


# Визуализируем результаты
visualize_spectrum(spectrum, mu, R)

# print(f"Центр окружности μ: {mu:.6f}")
# print(f"Радиус R: {R:.6f}")
# print(f"Спектральный радиус: {R / abs(mu):.6f}")
# print(f"Число итераций: {iterations}")
# print(f"Сошелся: {'Да' if converged else 'Нет'}")

# for i, xi in enumerate(solution):
#     print(i, xi)
# print()
# print(solution)