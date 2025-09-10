def create_matrix(n):
    return [[0.0] * n for _ in range(n)]


def copy_matrix(src):
    n = len(src)
    dest = create_matrix(n)
    for i in range(n):
        for j in range(n):
            dest[i][j] = src[i][j]
    return dest


def determinant(matrix):
    n = len(matrix)

    if n == 1:
        return matrix[0][0]

    det = 0
    for col in range(n):
        submatrix = create_matrix(n - 1)
        sub_i = 0
        for i in range(1, n):
            sub_j = 0
            for j in range(n):
                if j == col:
                    continue
                submatrix[sub_i][sub_j] = matrix[i][j]
                sub_j += 1
            sub_i += 1

        if col % 2 == 0:
            sign = 1
        else:
            sign = -1
        det += sign * matrix[0][col] * determinant(submatrix)

    return det


def cofactor_matrix(matrix):
    n = len(matrix)
    cofactor = create_matrix(n)

    if n == 1:
        cofactor[0][0] = 1
        return cofactor

    for i in range(n):
        for j in range(n):
            submatrix = create_matrix(n - 1)
            sub_i = 0
            for ii in range(n):
                if ii == i:
                    continue
                sub_j = 0
                for jj in range(n):
                    if jj == j:
                        continue
                    submatrix[sub_i][sub_j] = matrix[ii][jj]
                    sub_j += 1
                sub_i += 1

            if (i + j) % 2 == 0:
                sign = 1
            else:
                sign = -1
            cofactor[i][j] = sign * determinant(submatrix)

    return cofactor


def transpose_matrix(matrix):
    n = len(matrix)
    transposed = create_matrix(n)
    for i in range(n):
        for j in range(n):
            transposed[j][i] = matrix[i][j]
    return transposed


def scalar_matrix_multiply(matrix, scalar):
    n = len(matrix)
    result = create_matrix(n)
    for i in range(n):
        for j in range(n):
            result[i][j] = matrix[i][j] * scalar
    return result


def matrix_vector_multiply(matrix, vector):
    n = len(matrix)
    result = [0.0] * n
    for i in range(n):
        for j in range(n):
            result[i] += matrix[i][j] * vector[j]
    return result


def main():
    n = int(input("Введите размерность матрицы: "))

    print(f"Введите элементы матрицы A ({n}x{n}):")
    A = create_matrix(n)
    for i in range(n):
        row = list(map(float, input().split()))
        for j in range(n):
            A[i][j] = row[j]

    print("Введите элементы вектора B:")
    B = list(map(float, input().split()))

    det = determinant(A)
    if abs(det) < 1e-10:
        print("Матрица вырожденная, система не имеет единственного решения")
        return

    cofactor = cofactor_matrix(A)
    adjoint = transpose_matrix(cofactor)
    A_inv = scalar_matrix_multiply(adjoint, 1.0 / det)

    X = matrix_vector_multiply(A_inv, B)

    print("Решение X:")
    for i in range(n):
        print(f"x{i + 1} = {X[i]:.6f}")


if __name__ == "__main__":
    main()
