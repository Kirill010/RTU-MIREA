#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 3
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

// Упрощенный двухшаговый метод градиентного спуска
void two_step_gradient_descent(double** A, double* f, double* u, int* iterations,
                              double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    double* r = allocate_vector(size);     // невязка r = (I + A)u - f
    double* Ar = allocate_vector(size);    // A * r
    double* I_plus_A_u = allocate_vector(size); // (I + A)u
    double* u_prev = allocate_vector(size); // u_{k-1}
    double* r_prev = allocate_vector(size); // r_{k-1}

    *iterations = 0;
    *matrix_multiplies = 0;

    // Начальное приближение u0 = 0
    for (int i = 0; i < size; i++) {
        u[i] = 0.0;
        u_prev[i] = 0.0;
    }

    // Первая итерация - обычный градиентный спуск
    if (MAX_ITER > 0) {
        // r0 = (I + A)u0 - f = -f (т.к. u0 = 0)
        for (int i = 0; i < size; i++) {
            r[i] = -f[i];
        }

        // A * r
        matrix_vector_mult(A, r, Ar, size); (*matrix_multiplies)++;

        // Вычисляем шаг α
        double numerator = dot_product(r, r, size);
        double denominator = 0.0;
        for (int i = 0; i < size; i++) {
            denominator += (r[i] + Ar[i]) * (r[i] + Ar[i]);
        }

        if (denominator > 1e-15) {
            double alpha = numerator / denominator;
            for (int i = 0; i < size; i++) {
                u[i] = u_prev[i] - alpha * (r[i] + Ar[i]);
            }
        }

        (*iterations) = 1;
    }

    // Сохраняем предыдущие значения
    for (int i = 0; i < size; i++) {
        u_prev[i] = u[i];
        r_prev[i] = r[i];
    }

    // Основной цикл итераций
    for (int k = 1; k < MAX_ITER; k++) {
        // Вычисляем невязку r_k
        matrix_vector_mult(A, u, I_plus_A_u, size); (*matrix_multiplies)++;
        for (int i = 0; i < size; i++) {
            r[i] = u[i] + I_plus_A_u[i] - f[i];
        }

        // A * r_k
        matrix_vector_mult(A, r, Ar, size); (*matrix_multiplies)++;

        // Вычисляем оптимальные параметры
        double rr = dot_product(r, r, size);
        double r_prev_r_prev = dot_product(r_prev, r_prev, size);

        // Простой двухшаговый метод с рестартом
        double beta = (rr > 1e-15 && r_prev_r_prev > 1e-15) ? rr / r_prev_r_prev : 0.0;

        // Ограничиваем beta для стабильности
        if (beta > 1.0) beta = 0.0;

        // Обновление: u_{k+1} = u_k - α*(r + Ar) + β*(u_k - u_{k-1})
        double numerator = dot_product(r, r, size);
        double denominator = 0.0;
        for (int i = 0; i < size; i++) {
            denominator += (r[i] + Ar[i]) * (r[i] + Ar[i]);
        }

        if (denominator > 1e-15) {
            double alpha = numerator / denominator;

            for (int i = 0; i < size; i++) {
                double new_u = u[i] - alpha * (r[i] + Ar[i]) + beta * (u[i] - u_prev[i]);
                u_prev[i] = u[i];
                u[i] = new_u;
            }
        }

        // Обновляем предыдущую невязку
        for (int i = 0; i < size; i++) {
            r_prev[i] = r[i];
        }

        // Проверка сходимости по невязке
        double residual_norm = vector_norm(r, size);
        double f_norm = vector_norm(f, size);
        if (f_norm < 1e-15) f_norm = 1.0;

        if (residual_norm / f_norm < EPSILON) {
            *iterations = k + 1;
            break;
        }

        // Защита от расходимости
        if (residual_norm > 1e10 || isnan(residual_norm)) {
            printf("Two-step method diverges! Stopping at iteration %d\n", k+1);
            break;
        }

        *iterations = k + 1;
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free(r);
    free(Ar);
    free(I_plus_A_u);
    free(u_prev);
    free(r_prev);
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

    // Двухшаговый метод градиентного спуска
    double* u_ts = allocate_vector(N);
    int iter_ts = 0, mult_ts = 0;
    double time_ts = 0.0;
    two_step_gradient_descent(A_integral, f, u_ts, &iter_ts, &time_ts, &mult_ts, N);
    double error_ts = compute_error(u_ts, u_analytical, N);

    printf("Two-Step Gradient Descent:\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_ts, mult_ts, time_ts, error_ts);

    printf("Performance Comparison:\n");
    printf("Method           Iterations  Matrix Mults  Time (sec)  Error\n");
    printf("Simple Iter      %-11d %-13d %-11.6f %.10e\n",
           iter_si, mult_si, time_si, error_si);
    printf("Gradient Descent %-11d %-13d %-11.6f %.10e\n",
           iter_gd, mult_gd, time_gd, error_gd);
    printf("Two-Step GD      %-11d %-13d %-11.6f %.10e\n",
           iter_ts, mult_ts, time_ts, error_ts);

    free(x);
    free_matrix(A_integral, N);
    free(f);
    free(u_analytical);
    free(u_si);
    free(u_gd);
    free(u_ts);

    return 0;
}
