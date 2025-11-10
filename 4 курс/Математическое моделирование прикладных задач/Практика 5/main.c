#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 10
#define EPSILON 1e-6
#define MAX_ITER 100000

double** allocate_matrix(int rows, int cols) {
    double** matrix = (double**)malloc(rows * sizeof(double*));
    if (!matrix) {
        fprintf(stderr, "Memory alloc failed (matrix pointers)\n");
        exit(EXIT_FAILURE);
    }
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double*)calloc(cols, sizeof(double));
        if (!matrix[i]) {
            fprintf(stderr, "Memory alloc failed (matrix row)\n");
            exit(EXIT_FAILURE);
        }
    }
    return matrix;
}

void free_matrix(double** matrix, int rows) {
    if (!matrix) return;
    for (int i = 0; i < rows; i++) free(matrix[i]);
    free(matrix);
}

double* allocate_vector(int size) {
    double* v = (double*)calloc(size, sizeof(double));
    if (!v) {
        fprintf(stderr, "Memory alloc failed (vector)\n");
        exit(EXIT_FAILURE);
    }
    return v;
}

double vector_norm(const double* v, int size) {
    double sum = 0.0;
    for (int i = 0; i < size; i++) sum += v[i] * v[i];
    return sqrt(sum);
}

void matrix_vector_mult(double** A, const double* v, double* result, int size) {
    for (int i = 0; i < size; i++) {
        double s = 0.0;
        double* Ai = A[i];
        for (int j = 0; j < size; j++) s += Ai[j] * v[j];
        result[i] = s;
    }
}

double dot_product(const double* a, const double* b, int size) {
    double r = 0.0;
    for (int i = 0; i < size; i++) r += a[i] * b[i];
    return r;
}

// аналитическое решение для этого ядра/задачи
double analytical_solution(double x) {
    return 1.5 * x;
}

// Метод бисопряженных градиентов (BiCG)
void bicg(double** A, double* f, double* u, int* iterations,
          double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    *iterations = 0;
    *matrix_multiplies = 0;

    // Выделение памяти для рабочих векторов
    double* r = allocate_vector(size);      // невязка r = f - A*u
    double* r_tilde = allocate_vector(size); // вспомогательная невязка
    double* p = allocate_vector(size);      // направление поиска
    double* p_tilde = allocate_vector(size); // вспомогательное направление
    double* Ap = allocate_vector(size);     // A*p
    double* A_T_p_tilde = allocate_vector(size); // A^T * p_tilde
    double* v = allocate_vector(size);

    // Инициализация
    // Начальное приближение u0 = 0
    for (int i = 0; i < size; i++) {
        u[i] = 0.0;
    }

    // r0 = f - A*u0 = f
    for (int i = 0; i < size; i++) {
        r[i] = f[i];
        r_tilde[i] = f[i]; // r̃0 = r0
        p[i] = r[i];
        p_tilde[i] = r_tilde[i];
    }

    double rho_prev = 1.0;

    for (int k = 0; k < MAX_ITER; k++) {
        // ρ_k = (r̃_{k-1}, r_{k-1})
        double rho = dot_product(r_tilde, r, size);

        if (fabs(rho) < 1e-15) {
            printf("BiCG: Breakdown at iteration %d (rho=0)\n", k);
            break;
        }

        // v = A*p
        matrix_vector_mult(A, p, v, size);
        (*matrix_multiplies)++;

        // α = ρ_{k-1} / (r̃_0, v)
        double alpha = rho / dot_product(r_tilde, v, size);

        // u_k = u_{k-1} + α * p
        for (int i = 0; i < size; i++) {
            u[i] += alpha * p[i];
        }

        // r_k = r_{k-1} - α * v
        for (int i = 0; i < size; i++) {
            r[i] -= alpha * v[i];
        }

        // A^T * p_tilde (для симметричной матрицы A^T = A)
        matrix_vector_mult(A, p_tilde, A_T_p_tilde, size);
        (*matrix_multiplies)++;

        // r_tilde_k = r_tilde_{k-1} - α * A^T * p_tilde
        for (int i = 0; i < size; i++) {
            r_tilde[i] -= alpha * A_T_p_tilde[i];
        }

        // β = (r̃_k, r_k) / ρ_{k-1}
        double rho_new = dot_product(r_tilde, r, size);
        double beta = rho_new / rho;

        // p_{k+1} = r_k + β * p_k
        for (int i = 0; i < size; i++) {
            p[i] = r[i] + beta * p[i];
        }

        // p_tilde_{k+1} = r_tilde_k + β * p_tilde_k
        for (int i = 0; i < size; i++) {
            p_tilde[i] = r_tilde[i] + beta * p_tilde[i];
        }

        // Проверка сходимости
        double residual_norm = vector_norm(r, size);
        double f_norm = vector_norm(f, size);
        if (f_norm < 1e-15) f_norm = 1.0;

        if (residual_norm / f_norm < EPSILON) {
            *iterations = k + 1;
            break;
        }

        rho_prev = rho;
        *iterations = k + 1;

        // Защита от расходимости
        if (residual_norm > 1e10 || isnan(residual_norm)) {
            printf("BiCG diverges! Stopping at iteration %d\n", k+1);
            break;
        }
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free(r);
    free(r_tilde);
    free(p);
    free(p_tilde);
    free(Ap);
    free(A_T_p_tilde);
    free(v);
}

// Стабилизированный метод бисопряженных градиентов (BiCGSTAB)
void bicgstab(double** A, double* f, double* u, int* iterations,
              double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    *iterations = 0;
    *matrix_multiplies = 0;

    // Выделение памяти для рабочих векторов
    double* r = allocate_vector(size);      // невязка
    double* r_tilde = allocate_vector(size); // вспомогательный вектор
    double* p = allocate_vector(size);
    double* v = allocate_vector(size);
    double* s = allocate_vector(size);
    double* t = allocate_vector(size);

    // Инициализация
    for (int i = 0; i < size; i++) {
        u[i] = 0.0;
        p[i] = 0.0;
        v[i] = 0.0;
    }

    // r0 = f - A*u0 = f
    for (int i = 0; i < size; i++) {
        r[i] = f[i];
        r_tilde[i] = r[i]; // r̃ = r0
    }

    double rho_prev = 1.0, alpha = 1.0, omega = 1.0;

    for (int k = 0; k < MAX_ITER; k++) {
        // ρ_k = (r̃, r_{k-1})
        double rho = dot_product(r_tilde, r, size);

        if (fabs(rho) < 1e-15) {
            printf("BiCGSTAB: Breakdown at iteration %d (rho=0)\n", k);
            break;
        }

        // β = (ρ_k / ρ_{k-1}) * (α / ω_{k-1})
        double beta = (rho / rho_prev) * (alpha / omega);

        // p_k = r_{k-1} + β * (p_{k-1} - ω_{k-1} * v_{k-1})
        for (int i = 0; i < size; i++) {
            p[i] = r[i] + beta * (p[i] - omega * v[i]);
        }

        // v_k = A * p_k
        matrix_vector_mult(A, p, v, size);
        (*matrix_multiplies)++;

        // α = ρ_k / (r̃, v_k)
        alpha = rho / dot_product(r_tilde, v, size);

        // s = r_{k-1} - α * v_k
        for (int i = 0; i < size; i++) {
            s[i] = r[i] - alpha * v[i];
        }

        // t = A * s
        matrix_vector_mult(A, s, t, size);
        (*matrix_multiplies)++;

        // ω = (t, s) / (t, t)
        double ts = dot_product(t, s, size);
        double tt = dot_product(t, t, size);
        omega = (fabs(tt) > 1e-15) ? (ts / tt) : 0.0;

        // u_k = u_{k-1} + α * p_k + ω * s
        for (int i = 0; i < size; i++) {
            u[i] += alpha * p[i] + omega * s[i];
        }

        // r_k = s - ω * t
        for (int i = 0; i < size; i++) {
            r[i] = s[i] - omega * t[i];
        }

        // Проверка сходимости
        double residual_norm = vector_norm(r, size);
        double f_norm = vector_norm(f, size);
        if (f_norm < 1e-15) f_norm = 1.0;

        if (residual_norm / f_norm < EPSILON) {
            *iterations = k + 1;
            break;
        }

        rho_prev = rho;
        *iterations = k + 1;

        // Защита от расходимости
        if (residual_norm > 1e10 || isnan(residual_norm)) {
            printf("BiCGSTAB diverges! Stopping at iteration %d\n", k+1);
            break;
        }
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free(r);
    free(r_tilde);
    free(p);
    free(v);
    free(s);
    free(t);
}

// простая итерация для уравнения u + Au = f
void simple_iteration(double** A, double* f, double* u, int* iterations,
                      double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    double* u_new = allocate_vector(size);
    double* Au = allocate_vector(size);

    *iterations = 0;
    *matrix_multiplies = 0;

    for (int k = 0; k < MAX_ITER; k++) {
        // Au = A * u
        matrix_vector_mult(A, u, Au, size);
        (*matrix_multiplies)++;

        // u_new = f - Au (т.к. u + Au = f => u = f - Au)
        for (int i = 0; i < size; i++) {
            u_new[i] = f[i] - Au[i];
        }

        // Проверка сходимости: ||u_new - u|| / ||u_new|| < ε
        double diff_norm = 0.0;
        double new_norm = 0.0;
        for (int i = 0; i < size; i++) {
            double diff = u_new[i] - u[i];
            diff_norm += diff * diff;
            new_norm += u_new[i] * u_new[i];
        }
        diff_norm = sqrt(diff_norm);
        new_norm = sqrt(new_norm);

        if (new_norm < 1e-15) new_norm = 1.0;

        if (diff_norm / new_norm < EPSILON) {
            *iterations = k + 1;
            // Копируем окончательное решение
            for (int i = 0; i < size; i++) u[i] = u_new[i];
            break;
        }

        // Обновляем u
        for (int i = 0; i < size; i++) {
            u[i] = u_new[i];
        }
        *iterations = k + 1;

        // Защита от расходимости
        if (vector_norm(u, size) > 1e10) {
            printf("Simple iteration diverges! Stopping at iteration %d\n", k+1);
            break;
        }
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free(u_new);
    free(Au);
}

// Метод градиентного спуска для уравнения u + Au = f
void gradient_descent(double** A, double* f, double* u, int* iterations,
                     double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    double* r = allocate_vector(size);  // невязка r = (I + A)u - f
    double* Ar = allocate_vector(size); // A * r
    double* I_plus_A_u = allocate_vector(size); // (I + A)u

    *iterations = 0;
    *matrix_multiplies = 0;

    // Начальное приближение u0 = 0
    for (int i = 0; i < size; i++) {
        u[i] = 0.0;
    }

    for (int k = 0; k < MAX_ITER; k++) {
        // r = (I + A)u - f
        matrix_vector_mult(A, u, I_plus_A_u, size); (*matrix_multiplies)++;
        for (int i = 0; i < size; i++) {
            r[i] = u[i] + I_plus_A_u[i] - f[i];
        }

        // Градиент: g = (I + A^T)r = r + A^T r
        // Но так как A симметричная, то A^T = A
        matrix_vector_mult(A, r, Ar, size); (*matrix_multiplies)++;

        // Вычисляем шаг α
        double numerator = dot_product(r, r, size);
        double denominator = 0.0;
        for (int i = 0; i < size; i++) {
            denominator += (r[i] + Ar[i]) * (r[i] + Ar[i]);
        }

        if (denominator < 1e-15) break;
        double alpha = numerator / denominator;

        // Обновление: u_{k+1} = u_k - α * g
        for (int i = 0; i < size; i++) {
            u[i] = u[i] - alpha * (r[i] + Ar[i]);
        }

        // Проверка сходимости по невязке
        double residual_norm = vector_norm(r, size);
        double f_norm = vector_norm(f, size);
        if (f_norm < 1e-15) f_norm = 1.0;

        if (residual_norm / f_norm < EPSILON) {
            *iterations = k + 1;
            break;
        }

        *iterations = k + 1;
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free(r);
    free(Ar);
    free(I_plus_A_u);
}

double compute_error(double* u_num, double* u_analytical, int size) {
    double num = 0.0, denom = 0.0;
    for (int i = 0; i < size; i++) {
        double d = u_num[i] - u_analytical[i];
        num += d * d;
        denom += u_analytical[i] * u_analytical[i];
    }
    if (denom < 1e-15) return sqrt(num);
    return sqrt(num / denom);
}

int main(void) {
    double a = 0.0, b = 1.0;
    double lambda_val = 1.0;
    double h = (b - a) / (double)N;

    // точки коллокации
    double* x = allocate_vector(N);
    for (int i = 0; i < N; i++) x[i] = a + h * (i + 0.5);

    // Матрица A для интегрального оператора (без единичной матрицы!)
    double** A_integral = allocate_matrix(N, N);
    double* f = allocate_vector(N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            // Интегральный оператор: A_ij = λ * h * K(x_i, x_j) = 1.0 * h * x[i] * x[j]
            A_integral[i][j] = lambda_val * h * x[i] * x[j];
        }
        f[i] = x[i]; // правая часть f(x) = x
    }

    double* u_analytical = allocate_vector(N);
    for (int i = 0; i < N; i++) u_analytical[i] = analytical_solution(x[i]);

    printf("N = %d\n", N);
    printf("eps = %e\n\n", EPSILON);

    // Простая итерация
    double* u_si = allocate_vector(N);
    int iter_si = 0, mult_si = 0;
    double time_si = 0.0;
    simple_iteration(A_integral, f, u_si, &iter_si, &time_si, &mult_si, N);
    double error_si = compute_error(u_si, u_analytical, N);

    printf("Simple Iteration Method:\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_si, mult_si, time_si, error_si);

    // Градиентный спуск
    double* u_gd = allocate_vector(N);
    int iter_gd = 0, mult_gd = 0;
    double time_gd = 0.0;
    gradient_descent(A_integral, f, u_gd, &iter_gd, &time_gd, &mult_gd, N);
    double error_gd = compute_error(u_gd, u_analytical, N);

    printf("Gradient Descent Method:\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_gd, mult_gd, time_gd, error_gd);

    // Метод бисопряженных градиентов (BiCG)
    double* u_bicg = allocate_vector(N);
    int iter_bicg = 0, mult_bicg = 0;
    double time_bicg = 0.0;
    bicg(A_integral, f, u_bicg, &iter_bicg, &time_bicg, &mult_bicg, N);
    double error_bicg = compute_error(u_bicg, u_analytical, N);

    printf("BiConjugate Gradient Method (BiCG):\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_bicg, mult_bicg, time_bicg, error_bicg);

    // Стабилизированный метод бисопряженных градиентов (BiCGSTAB)
    double* u_bicgstab = allocate_vector(N);
    int iter_bicgstab = 0, mult_bicgstab = 0;
    double time_bicgstab = 0.0;
    bicgstab(A_integral, f, u_bicgstab, &iter_bicgstab, &time_bicgstab, &mult_bicgstab, N);
    double error_bicgstab = compute_error(u_bicgstab, u_analytical, N);

    printf("Stabilized BiConjugate Gradient Method (BiCGSTAB):\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_bicgstab, mult_bicgstab, time_bicgstab, error_bicgstab);

    printf("Performance Comparison:\n");
    printf("Method           Iterations  Matrix Mults  Time (sec)  Error\n");
    printf("Simple Iter      %-11d %-13d %-11.6f %.10e\n",
           iter_si, mult_si, time_si, error_si);
    printf("Gradient Descent %-11d %-13d %-11.6f %.10e\n",
           iter_gd, mult_gd, time_gd, error_gd);
    printf("BiCG             %-11d %-13d %-11.6f %.10e\n",
           iter_bicg, mult_bicg, time_bicg, error_bicg);
    printf("BiCGSTAB         %-11d %-13d %-11.6f %.10e\n",
           iter_bicgstab, mult_bicgstab, time_bicgstab, error_bicgstab);

    free(x);
    free_matrix(A_integral, N);
    free(f);
    free(u_analytical);
    free(u_si);
    free(u_gd);
    free(u_bicg);
    free(u_bicgstab);

    return 0;
}
