#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
#include <locale.h>

#define A_VAL 0.0
#define B_VAL 1.0
#define N 3
#define lambda_val 1.0
#define epsilon 1e-6
#define max_iter 1000

double analytical_solution(double x)
{
    return (-425.0 / 63.0) * x * x * x + x * x * x * x * x - 1.0;
}

double kernel(double x, double t)
{
    return x * x * x * (2 + t);
}

double f_function(double x)
{
    return x * x * x * x * x - 1.0;
}

void matrix_vector_mult(double A[N][N], double x[N], double result[N])
{
    for (int i = 0; i < N; i++)
    {
        result[i] = 0.0;
        for (int j = 0; j < N; j++)
        {
            result[i] += A[i][j] * x[j];
        }
    }
}

void vector_sub(double vec1[N], double vec2[N], double result[N])
{
    for (int i = 0; i < N; i++)
    {
        result[i] = vec1[i] - vec2[i];
    }
}

double vector_norm(double v[N])
{
    double sum = 0.0;
    for (int i = 0; i < N; i++)
    {
        sum += v[i] * v[i];
    }
    return sqrt(sum);
}

double vector_abs_sum(double v[N])
{
    double sum = 0.0;
    for (int i = 0; i < N; i++)
    {
        sum += fabs(v[i]);
    }
    return sum;
}

int main()
{
    setlocale(LC_ALL, "");
    double h = (B_VAL - A_VAL) / N;

    double x[N];
    for (int i = 0; i < N; i++)
    {
        x[i] = i * h + h / 2.0 + A_VAL;
    }

    double y_analytical[N];
    for (int i = 0; i < N; i++)
    {
        y_analytical[i] = analytical_solution(x[i]);
    }

    double A[N][N], f[N];

    for (int i = 0; i < N; i++)
    {
        f[i] = f_function(x[i]);

        for (int j = 0; j < N; j++)
        {
            A[i][j] = -lambda_val * h * kernel(x[i], x[j]);
        }
        A[i][i] += 1.0;
    }

    double M = 0.0;
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            if (fabs(A[i][j]) > M)
            {
                M = fabs(A[i][j]);
            }
        }
        if (fabs(f[i]) > M)
        {
            M = fabs(f[i]);
        }
    }

    double A_norm[N][N], f_norm[N];
    for (int i = 0; i < N; i++)
    {
        f_norm[i] = f[i] / M;
        for (int j = 0; j < N; j++)
        {
            A_norm[i][j] = A[i][j] / M;
        }
    }

    double B[N][N];
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
        {
            B[i][j] = -A_norm[i][j];
        }
        B[i][i] += 1.0;
    }

    double y_prev[N], y_iter[N], temp[N];
    int k;

    for (int i = 0; i < N; i++)
    {
        y_prev[i] = f_norm[i];
    }

    for (k = 0; k < max_iter; k++)
    {
        matrix_vector_mult(B, y_prev, temp);
        for (int i = 0; i < N; i++)
        {
            y_iter[i] = temp[i] + f_norm[i];
        }

        double diff[N];
        vector_sub(y_iter, y_prev, diff);

        if (vector_norm(diff) < epsilon)
        {
            break;
        }

        memcpy(y_prev, y_iter, sizeof(double) * N);
    }

    double diff_analytical[N];
    vector_sub(y_analytical, y_iter, diff_analytical);
    double error = vector_abs_sum(diff_analytical) / vector_abs_sum(y_analytical);

    printf("Integral equation: y(x) = (2+t)*x^3*y(t)dt + x^5 - 1\n");
    printf("Collocation points (x): ");
    for (int i = 0; i < N; i++)
    {
        printf("%.6f ", x[i]);
    }
    printf("\n\n");

    printf("Analytical solution y(x) = x^5 - 1:\n");
    for (int i = 0; i < N; i++)
    {
        printf("y(%.3f) = %.6f\n", x[i], y_analytical[i]);
    }
    printf("\n");

    printf("Numerical solution:\n");
    for (int i = 0; i < N; i++)
    {
        printf("y_num(%.3f) = %.6f\n", x[i], y_iter[i]);
    }
    printf("\n");

    printf("Number of iterations: %d\n", k + 1);
    printf("Relative error: %.6f%%\n", error * 100);

    return 0;
}
