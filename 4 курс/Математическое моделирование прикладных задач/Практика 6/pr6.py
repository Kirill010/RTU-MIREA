"""
Улучшённый скрипт (обновлённый):
- поиск μ: перебор пар -> перебор троек -> MEC (Welzl)
- безопасный подбор итерационного параметра τ (на основе μ и spectrum), fallback'ы
- стабильная итерация с проверкой на overflow/NaN
- один аккуратный график: Краевые точки (ordered polygon), выбранная окружность (μ,R), центр μ
  (Спектр на графике НЕ отображается по запросу.)
"""
import numpy as np
import matplotlib.pyplot as plt
import random, math
from typing import List, Tuple, Optional

# -------------------- Геометрия: окружности --------------------
def circle_from_2(p1: complex, p2: complex) -> Tuple[complex, float]:
    c = (p1 + p2) / 2
    return c, abs(p1 - c)

def circle_from_3(p1: complex, p2: complex, p3: complex) -> Tuple[Optional[complex], Optional[float]]:
    x1,y1 = p1.real, p1.imag
    x2,y2 = p2.real, p2.imag
    x3,y3 = p3.real, p3.imag
    M = np.array([[x1,y1,1.0],[x2,y2,1.0],[x3,y3,1.0]])
    detM = np.linalg.det(M)
    if abs(detM) < 1e-14:
        return None, None
    def sq(x,y): return x*x + y*y
    ox = np.linalg.det(np.array([[sq(x1,y1), y1, 1.0],
                                 [sq(x2,y2), y2, 1.0],
                                 [sq(x3,y3), y3, 1.0]]))
    oy = np.linalg.det(np.array([[sq(x1,y1), x1, 1.0],
                                 [sq(x2,y2), x2, 1.0],
                                 [sq(x3,y3), x3, 1.0]]))
    cx = ox / (2 * detM)
    cy = - oy / (2 * detM)
    c = complex(cx, cy)
    return c, abs(c - p1)

def covers_all(c: complex, r: float, pts: List[complex], eps: float = 1e-12) -> bool:
    return np.all(np.abs(np.array(pts) - c) <= r + eps)

# -------------------- Минимальная охватывающая окружность (Welzl) --------------------
def mec_welzl(points: List[complex], rng_seed: Optional[int] = None) -> Tuple[complex, float]:
    pts = points.copy()
    if rng_seed is not None:
        random.seed(rng_seed)
    random.shuffle(pts)
    def c2(a,b): return (a+b)/2, abs(a-(a+b)/2)
    def c3(a,b,c):
        res = circle_from_3(a,b,c)
        if res[0] is None:
            # вернём окружность по наиболее удалённой паре
            pair = (a,b); md = abs(a-b)
            for P in (a,b,c):
                for Q in (a,b,c):
                    if P is Q: continue
                    d = abs(P-Q)
                    if d > md:
                        md = d; pair = (P,Q)
            return c2(*pair)
        return res
    def rec(sub,bound):
        if not sub or len(bound) == 3:
            if len(bound) == 0: return complex(0,0), -1.0
            if len(bound) == 1: return bound[0], 0.0
            if len(bound) == 2: return c2(bound[0], bound[1])
            return c3(bound[0], bound[1], bound[2])
        p = sub.pop()
        c,r = rec(sub,bound)
        if r >= 0 and abs(p - c) <= r + 1e-12:
            sub.append(p); return c,r
        bound.append(p)
        cres = rec(sub,bound)
        bound.pop(); sub.append(p)
        return cres
    return rec(pts, [])

# -------------------- Генерация boundary и spectrum --------------------
def random_boundary_points(m:int, center_range=(0,10), radius_range=(2,8),
                           irregularity:float=0.4, prob_real:float=0.2, seed:Optional[int]=None) -> List[complex]:
    if seed is not None:
        np.random.seed(seed); random.seed(seed)
    cx = np.random.uniform(center_range[0], center_range[1])
    cy = np.random.uniform(center_range[0], center_range[1])
    center = complex(cx, cy)
    base_r = np.random.uniform(radius_range[0], radius_range[1])
    angles = np.linspace(0, 2*np.pi, m, endpoint=False)
    pts=[]
    for theta in angles:
        dr = irregularity * base_r * (np.random.rand() - 0.5) * 2
        dtheta = (np.random.rand() - 0.5) * (np.pi * irregularity / max(1,m))
        r = max(0.05, base_r + dr)
        t = theta + dtheta
        if np.random.rand() < prob_real:
            x = center.real + r*math.cos(t)
            pts.append(complex(x,0.0))
        else:
            pts.append(center + r*complex(math.cos(t), math.sin(t)))
    return pts

def generate_spectrum_and_A(boundary:List[complex], n:int, interior_count:Optional[int]=None,
                            fraction_real_interior:float=0.3, seed:Optional[int]=None) -> Tuple[np.ndarray,np.ndarray,complex,float]:
    if seed is not None:
        np.random.seed(seed); random.seed(seed)
    center_b, radius_b = mec_welzl(boundary, rng_seed=seed)
    if interior_count is None:
        interior_count = max(0, n - len(boundary))
    interior=[]
    for _ in range(interior_count):
        rr = radius_b * math.sqrt(np.random.rand())
        theta = 2*math.pi*np.random.rand()
        if np.random.rand() < fraction_real_interior:
            real_part = center_b.real + rr*math.cos(theta)
            interior.append(complex(real_part, 0.0))
        else:
            interior.append(center_b + rr*complex(math.cos(theta), math.sin(theta)))
    spectrum = list(boundary) + interior
    while len(spectrum) < n:
        spectrum.append(random.choice(boundary))
    spectrum = np.array(spectrum[:n], dtype=complex)
    A = np.diag(spectrum)
    return spectrum, A, center_b, radius_b

# -------------------- Поиск μ: пары -> тройки -> MEC --------------------
def search_mu(boundary:List[complex]) -> Tuple[complex,float,str]:
    m = len(boundary)
    # перебор пар (центр середина)
    best=None
    for i in range(m):
        for j in range(i+1,m):
            c,R = circle_from_2(boundary[i], boundary[j])
            if covers_all(c,R,boundary):
                if best is None or R < best[1]:
                    best = (c,R,'pair')
    if best is not None: return best
    # перебор троек
    best=None
    for i in range(m):
        for j in range(i+1,m):
            for k in range(j+1,m):
                cR = circle_from_3(boundary[i], boundary[j], boundary[k])
                if cR[0] is None: continue
                c,R = cR
                if covers_all(c,R,boundary):
                    if best is None or R < best[1]:
                        best = (c,R,'triple')
    if best is not None: return best
    # иначе MEC
    c,R = mec_welzl(boundary)
    return c,R,'welzl'

# -------------------- Подбор безопасного tau (используя mu) --------------------
def choose_tau_from_mu(mu:complex, spectrum:np.ndarray) -> Tuple[complex,str]:
    lam = spectrum
    if abs(mu) < 1e-14:
        tau = 0.9 / np.max(np.abs(lam))
        return tau, 'scalar_due_to_mu_zero'
    z = mu * lam
    re_z = z.real
    abs_z2 = np.abs(z)**2
    if np.any(re_z <= 0):
        tau = 0.9 / np.max(np.abs(lam))
        return tau, 'scalar_fallback_re_z_nonpos'
    beta_i = 2.0 * re_z / (abs_z2 + 1e-30)
    beta_max = np.min(beta_i)
    if beta_max <= 0 or not np.isfinite(beta_max):
        tau = 0.9 / np.max(np.abs(lam))
        return tau, 'scalar_fallback_beta_nonpos'
    beta = 0.9 * beta_max
    tau = beta * mu
    return tau, 'scaled_mu'

# -------------------- Стабильная итерация (проверка NaN/inf) --------------------
def generalized_simple_iteration_safe(A:np.ndarray, f:np.ndarray, tau:complex, x0:Optional[np.ndarray]=None,
                                      tol:float=1e-9, max_iter:int=5000) -> Tuple[np.ndarray,int,bool]:
    n = A.shape[0]
    x = np.zeros(n, dtype=complex) if x0 is None else x0.copy().astype(complex)
    norm_f = np.linalg.norm(f)
    if norm_f == 0: norm_f = 1.0
    matvecs = 0
    for k in range(max_iter):
        Ax = A.dot(x); matvecs += 1
        r = f - Ax
        x_new = x + tau * r
        if not np.isfinite(x_new).all():
            return x_new, matvecs, False
        if np.linalg.norm(x_new - x) / norm_f < tol:
            return x_new, matvecs, True
        x = x_new
    return x, matvecs, False

# -------------------- Визуализация: сортировка по углу --------------------
def sort_by_angle(pts:List[complex], center:complex) -> np.ndarray:
    arr = np.array(pts, dtype=complex)
    ang = np.angle(arr - center)
    return arr[np.argsort(ang)]

# -------------------- main --------------------
def main():
    # Параметры
    random_seed = None     # None -> каждый запуск разный; число -> воспроизводимость
    m_boundary = 6
    n = 500

    # Генерация краевых точек и спектра (спектр не будет рисоваться по требованию)
    boundary = random_boundary_points(m_boundary, center_range=(0,12), radius_range=(2,8),
                                      irregularity=0.5, prob_real=0.25, seed=random_seed)
    spectrum, A, center_b, radius_b = generate_spectrum_and_A(boundary, n, interior_count=None,
                                                              fraction_real_interior=0.35, seed=random_seed)

    # Проверка на ноль в спектре
    if np.any(np.isclose(spectrum, 0.0, atol=1e-14)):
        raise RuntimeError("Спектр содержит значение, близкое к нулю. Итерационный метод не гарантирован.")

    # Поиск mu
    mu_candidate, R_candidate, method_mu = search_mu(boundary)
    print("Метод поиска μ:", method_mu)
    print("Кандидат μ:", mu_candidate, "R:", R_candidate)

    # Если окружность не покрывает весь spectrum — берём MEC по spectrum
    max_dist_spec = np.max(np.abs(spectrum - mu_candidate))
    if max_dist_spec > R_candidate + 1e-12:
        print("Кандидат не покрывает весь спектр, берём MEC по всему спектру.")
        mu_candidate, R_candidate = mec_welzl(list(spectrum), rng_seed=random_seed)
        method_mu = 'mec_all_spectrum'
        print("MEC (по всем точкам):", mu_candidate, R_candidate)

    # Если μ близко к нулю — fallback на MEC по всему спектру
    if abs(mu_candidate) < 1e-14:
        mu_candidate, R_candidate = mec_welzl(list(spectrum), rng_seed=random_seed)
        method_mu = 'mec_fallback'
        print("μ был ~0 — использован запасной MEC:", mu_candidate, R_candidate)

    # Подбор τ
    tau, tau_method = choose_tau_from_mu(mu_candidate, spectrum)
    print("Метод выбора τ:", tau_method)
    print("τ (используется):", tau)

    # Правый вектор f по заданию
    N = A.shape[0]
    f = 1j * np.arange(1, N+1, dtype=float)

    # Запуск итераций
    x0 = np.zeros(N, dtype=complex)
    x_sol, matvecs, converged = generalized_simple_iteration_safe(A, f, tau, x0=x0, tol=1e-9, max_iter=5000)
    if not converged:
        print("Основной τ не сошелся — пробуем безопасный скаляр τ.")
        tau_safe = 0.9 / np.max(np.abs(spectrum))
        x_sol, matvecs, converged = generalized_simple_iteration_safe(A, f, tau_safe, x0=x0, tol=1e-9, max_iter=5000)
        tau = tau_safe

    final_res = np.linalg.norm(f - A.dot(x_sol))
    print("Итоговое μ:", mu_candidate, "R:", R_candidate, "метод μ:", method_mu)
    print("Итоговый τ:", tau, "сошлось:", converged, "умножений A@x:", matvecs)
    print("Финальная невязка ||f - A x||:", final_res, "||x||:", np.linalg.norm(x_sol))

    # --- Визуализация (без спектра; подписи на русском) ---
    bp_sorted = sort_by_angle(boundary, mu_candidate)
    fig, ax = plt.subplots(figsize=(8,8))
    ax.set_aspect('equal','box')

    # краевые точки
    bp = np.array(boundary, dtype=complex)
    ax.scatter(bp.real, bp.imag, color='black', s=70, zorder=5, label='Краевые точки')

    # упорядоченный многоугольник границы
    ax.plot(np.append(bp_sorted.real, bp_sorted.real[0]), np.append(bp_sorted.imag, bp_sorted.imag[0]),
            color='gray', linestyle='-', linewidth=1, label='Многоугольник границы (упорядоченный)')

    # выбранная окружность (mu,R)
    th = np.linspace(0,2*np.pi,400)
    ax.plot(mu_candidate.real + R_candidate*np.cos(th), mu_candidate.imag + R_candidate*np.sin(th),
            color='blue', linewidth=2, label='Выбранная окружность (μ, R)')

    # центр μ
    ax.scatter([mu_candidate.real],[mu_candidate.imag], color='red', s=120, zorder=8, label='μ (центр)')

    # начало координат
    ax.scatter([0.0],[0.0], color='green', s=80, label='Начало координат')

    ax.set_xlabel("Re(λ) — действительная часть")
    ax.set_ylabel("Im(λ) — мнимая часть")
    ax.set_title("Краевые точки, выбранная окружность и центр μ")
    ax.grid(True); ax.legend(loc='upper right')
    plt.tight_layout(); plt.show()

if __name__ == "__main__":
    main()
