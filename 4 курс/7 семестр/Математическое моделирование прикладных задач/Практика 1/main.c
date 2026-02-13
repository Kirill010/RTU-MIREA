#include <stdio.h>
#include <stdlib.h>
#include <locale.h>

double** create_matrix(int n)
{
    double** matrix = (double**)malloc(n * sizeof(double*));
    for (int i = 0; i < n; i++)
    {
        matrix[i] = (double*)malloc(n * sizeof(double));
    }
    return matrix;
}

void free_matrix(double** matrix, int n)
{
    for (int i = 0; i < n; i++)
    {
        free(matrix[i]);
    }
    free(matrix);
}

void copy_matrix(double** src, double** dest, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            dest[i][j] = src[i][j];
        }
    }
}

double determinant(double** matrix, int n)
{
    if (n == 1)
    {
        return matrix[0][0];
    }

    double det = 0;
    double** submatrix = create_matrix(n - 1);

    for (int x = 0; x < n; x++)
    {
        int subi = 0;
        for (int i = 1; i < n; i++)
        {
            int subj = 0;
            for (int j = 0; j < n; j++)
            {
                if (j == x)
                {
                    continue;
                }
                submatrix[subi][subj] = matrix[i][j];
                subj++;
            }
            subi++;
        }

        double sign = 0;
        if (x % 2 == 0)
        {
            sign = 1;
        }
        else
        {
            sign = -1;
        }
        det += sign * matrix[0][x] * determinant(submatrix, n - 1);
    }

    free_matrix(submatrix, n - 1);
    return det;
}

void cofactor_matrix(double** matrix, double** cofactor, int n)
{
    if (n == 1)
    {
        cofactor[0][0] = 1;
        return;
    }

    double** temp = create_matrix(n - 1);

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            int subi = 0;
            for (int ii = 0; ii < n; ii++)
            {
                if (ii == i)
                {
                    continue;
                }
                int subj = 0;
                for (int jj = 0; jj < n; jj++)
                {
                    if (jj == j)
                    {
                        continue;
                    }
                    temp[subi][subj] = matrix[ii][jj];
                    subj++;
                }
                subi++;
            }

            double sign = 0;
            if ((i + j) % 2 == 0)
            {
                sign = 1;
            }
            else
            {
                sign = -1;
            }
            cofactor[i][j] = sign * determinant(temp, n - 1);
        }
    }

    free_matrix(temp, n - 1);
}

void transpose_matrix(double** matrix, double** result, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[j][i] = matrix[i][j];
        }
    }
}

void matrix_vector_multiply(double** matrix, double* vector, double* result, int n)
{
    for (int i = 0; i < n; i++)
    {
        result[i] = 0;
        for (int j = 0; j < n; j++)
        {
            result[i] += matrix[i][j] * vector[j];
        }
    }
}

void scalar_matrix_multiply(double** matrix, double scalar, double** result, int n)
{
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            result[i][j] = matrix[i][j] * scalar;
        }
    }
}

int main()
{
    int n;
    setlocale(LC_ALL, "Rus");
    printf("Введите размерность матрицы: ");
    scanf("%d", &n);

    double** A = create_matrix(n);
    double* B = (double*)malloc(n * sizeof(double));
    double* X = (double*)malloc(n * sizeof(double));

    printf("Введите элементы матрицы A (%dx%d):\n", n, n);
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            scanf("%lf", &A[i][j]);
        }
    }

    printf("Введите элементы вектора B:\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%lf", &B[i]);
    }

    double det = determinant(A, n);
    if (fabs(det) < 1e-10)
    {
        printf("Матрица вырожденная, система не имеет единственного решения.\n");
        return 1;
    }

    double** cofactor = create_matrix(n);
    double** adjoint = create_matrix(n);
    double** A_inv = create_matrix(n);

    cofactor_matrix(A, cofactor, n);
    transpose_matrix(cofactor, adjoint, n);
    scalar_matrix_multiply(adjoint, 1.0/det, A_inv, n);

    matrix_vector_multiply(A_inv, B, X, n);

    printf("Решение X:\n");
    for (int i = 0; i < n; i++)
    {
        printf("x%d = %.6f\n", i + 1, X[i]);
    }

    free_matrix(A, n);
    free_matrix(cofactor, n);
    free_matrix(adjoint, n);
    free_matrix(A_inv, n);
    free(B);
    free(X);

    return 0;
}
