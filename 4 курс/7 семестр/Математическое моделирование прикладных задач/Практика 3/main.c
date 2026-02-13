#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <time.h>

#define N 10
#define EPSILON 1e-6
#define MAX_ITER 10000

// Выделение памяти под матрицу
double** allocate_matrix(int rows, int cols) {
    double** matrix = (double**)malloc(rows * sizeof(double*));
    for (int i = 0; i < rows; i++) {
        matrix[i] = (double*)calloc(cols, sizeof(double));
    }
    return matrix;
}

// Освобождение памяти
void free_matrix(double** matrix, int rows) {
    for (int i = 0; i < rows; i++) free(matrix[i]);
    free(matrix);
}

// Выделение памяти под вектор
double* allocate_vector(int size) {
    return (double*)calloc(size, sizeof(double));
}

// Норма вектора
double vector_norm(double* v, int size) {
    double sum = 0.0;
    for (int i = 0; i < size; i++) {
        sum += v[i] * v[i];
    }
    return sqrt(sum);
}

// Умножение матрицы на вектор
void matrix_vector_mult(double** A, double* v, double* result, int size) {
    for (int i = 0; i < size; i++) {
        result[i] = 0.0;
        for (int j = 0; j < size; j++) {
            result[i] += A[i][j] * v[j];
        }
    }
}

// Аналитическое решение
double analytical_solution(double x) {
    // return 0.75 * x;
    return 1.5 * x;
}

// Метод простой итерации
void simple_iteration(double** A, double* f, double* u, int* iterations,
                     double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    double max_val = 0.0;
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            if (fabs(A[i][j]) > max_val) {
                max_val = fabs(A[i][j]);
            }
        }
        if (fabs(f[i]) > max_val) {
            max_val = fabs(f[i]);
        }
    }

    if (max_val == 0.0) {
        printf("Matrix and vector are zero — trivial solution.\n");
        return;
    }

    double** A_norm = allocate_matrix(size, size);
    double* f_norm = allocate_vector(size);

    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            A_norm[i][j] = A[i][j] / max_val;
        }
        f_norm[i] = f[i] / max_val;
    }

    double** B = allocate_matrix(size, size);
    for (int i = 0; i < size; i++) {
        for (int j = 0; j < size; j++) {
            B[i][j] = -A_norm[i][j];
        }
        B[i][i] += 1.0;
    }

    double* u_new = allocate_vector(size);
    double* temp = allocate_vector(size);

    *iterations = 0;
    *matrix_multiplies = 0;

    for (int k = 0; k < MAX_ITER; k++) {
        matrix_vector_mult(B, u, temp, size);
        (*matrix_multiplies)++;

        for (int i = 0; i < size; i++) {
            u_new[i] = temp[i] + f_norm[i];
        }

        double norm_diff = 0.0;
        for (int i = 0; i < size; i++) {
            norm_diff += (u_new[i] - u[i]) * (u_new[i] - u[i]);
        }
        norm_diff = sqrt(norm_diff);

        double norm_f = vector_norm(f_norm, size);
        if ((norm_f < 1e-14 && norm_diff < EPSILON) ||
            (norm_f >= 1e-14 && norm_diff / norm_f < EPSILON)) {
            *iterations = k + 1;
            break;
        }

        for (int i = 0; i < size; i++) {
            u[i] = u_new[i];
        }
        *iterations = k + 1;
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free_matrix(A_norm, size);
    free(f_norm);
    free_matrix(B, size);
    free(u_new);
    free(temp);
}

// Метод градиентного спуска
void gradient_descent(double** A, double* f, double* u, int* iterations,
                     double* time_spent, int* matrix_multiplies, int size) {
    clock_t start = clock();

    double* r = allocate_vector(size);
    double* g = allocate_vector(size);
    double* Ag = allocate_vector(size);
    double* u_new = allocate_vector(size);

    *iterations = 0;
    *matrix_multiplies = 0;

    for (int k = 0; k < MAX_ITER; k++) {
        // r = A*u - f
        matrix_vector_mult(A, u, r, size);
        (*matrix_multiplies)++;
        for (int i = 0; i < size; i++) {
            r[i] -= f[i];
        }

        // g = A**T * r
        matrix_vector_mult(A, r, g, size);
        (*matrix_multiplies)++;

        // Ag = A * g
        matrix_vector_mult(A, g, Ag, size);
        (*matrix_multiplies)++;

        // alpha = (g,g)/(Ag,Ag)
        double num = 0.0, den = 0.0;
        for (int i = 0; i < size; i++) {
            num += g[i] * g[i];
            den += Ag[i] * Ag[i];
        }

        if (den < 1e-15) break;
        double alpha = num / den;

        for (int i = 0; i < size; i++) {
            u_new[i] = u[i] - alpha * g[i];
        }

        double norm_diff = 0.0;
        for (int i = 0; i < size; i++) {
            norm_diff += (u_new[i] - u[i]) * (u_new[i] - u[i]);
        }
        norm_diff = sqrt(norm_diff);

        double norm_f = vector_norm(f, size);
        if ((norm_f < 1e-14 && norm_diff < EPSILON) ||
            (norm_f >= 1e-14 && norm_diff / norm_f < EPSILON)) {
            *iterations = k + 1;
            break;
        }

        for (int i = 0; i < size; i++) {
            u[i] = u_new[i];
        }
        *iterations = k + 1;
    }

    clock_t end = clock();
    *time_spent = ((double)(end - start)) / CLOCKS_PER_SEC;

    free(r);
    free(g);
    free(Ag);
    free(u_new);
}

// Ошибка
double compute_error(double* u_num, double* u_analytical, int size) {
    double num = 0.0, denom = 0.0;
    for (int i = 0; i < size; i++) {
        num += fabs(u_num[i] - u_analytical[i]);
        denom += fabs(u_analytical[i]);
    }
    if (denom < 1e-15) {
        return num;
    }
    return num / denom;
}

// Функция main
int main() {
    double a = 0.0, b = 1.0;
    double lambda_val = 1.0;
    double h = (b - a) / N;

    double* x = allocate_vector(N);
    for (int i = 0; i < N; i++) {
        x[i] = a + h * (i + 0.5);
    }

    double** A = allocate_matrix(N, N);
    double* f = allocate_vector(N);

    for (int i = 0; i < N; i++) {
        for (int j = 0; j < N; j++) {
            A[i][j] = lambda_val * h * x[i] * x[j];
        }
        A[i][i] += 1.0;
        f[i] = x[i];
    }

    double* u_analytical = allocate_vector(N);
    for (int i = 0; i < N; i++) {
        u_analytical[i] = analytical_solution(x[i]);
    }

    // Метод простой итерации
    double* u_si = allocate_vector(N);
    int iter_si = 0, mult_si = 0;
    double time_si = 0.0;
    simple_iteration(A, f, u_si, &iter_si, &time_si, &mult_si, N);
    double error_si = compute_error(u_si, u_analytical, N);

    // Метод градиентного спуска
    double* u_gd = allocate_vector(N);
    int iter_gd = 0, mult_gd = 0;
    double time_gd = 0.0;
    gradient_descent(A, f, u_gd, &iter_gd, &time_gd, &mult_gd, N);
    double error_gd = compute_error(u_gd, u_analytical, N);

    printf("N = %d\n", N);
    printf("eps = %e\n\n", EPSILON);

    printf("Simple Iteration Method:\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_si, mult_si, time_si, error_si);

    printf("Gradient Descent Method:\n");
    printf("  Iter: %d\n  Matrix mult: %d\n  Time: %.6f sec\n  Error: %.6e\n\n",
           iter_gd, mult_gd, time_gd, error_gd);

    printf("Performance Ratios (Grad_des / Simp_iter):\n");
    if (iter_si > 0 && mult_si > 0 && time_si > 0) {
        printf("  Iter ratio: %.2f\n", (double)iter_gd / iter_si);
        printf("  Mult ratio: %.2f\n", (double)mult_gd / mult_si);
        printf("  Time ratio: %.2f\n", time_gd / time_si);
    }

    free(x);
    free_matrix(A, N);
    free(f);
    free(u_analytical);
    free(u_si);
    free(u_gd);

    return 0;
}
