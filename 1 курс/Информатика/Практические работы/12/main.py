import random  # подключение библиотеки для реализации случайных чисел
import sys


def bubble_sort(tmp):
    for i in range(len(tmp) - 1):
        for j in range(len(tmp) - i - 1):
            if tmp[j] > tmp[j + 1]:
                tmp[j], tmp[j + 1] = tmp[j + 1], tmp[j]
    return tmp


numbers = ["1", "2", "3", "4", "5", "6", "7", "8", '9']
print("Введите размер матрицы")
M = int(input())  # размер матрицы M*M от 2 до 5
while (M < 2 or M > 5):
    print("Размер матрицы должен быть от 2 до 5!")
    M = int(input())
matrix = []  # объявление матрицы
tmp = []  # временный массив
print("Введите способ ввода матрицы (1 - случайные, 2 - пользователь вводит с клавиатуры)")
variant = int(input())  # пользователь выбирает вариант создания матрицы
while (variant != 1 and variant != 2):
    print("1 или 2!")
    variant = int(input())
if (variant == 1):
    for i in range(M):
        matrix.append([])
        for j in range(M):
            matrix[i].append(random.randint(1, 100))

    print()
    for i in range(M):  # вывод изначальной матрицы
        for j in range(M):
            print(matrix[i][j], end=" ")
        print()

    for i in range(len(matrix)):  # закидываю элементы выше побочной диагонали
        for j in range(len(matrix) - i):
            tmp.append(matrix[i][j])

    bubble_sort(tmp)  # сортируем элементы

    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            matrix[i][j] = tmp[k]
            k += 1
            if (k == len(tmp)):
                break

else:
    for i in range(M):  # наполнение матрицы пользовательскими числами
        p = []
        for j in range(M):
            print(f"Введите значения [{i};{j}]")
            qtty = input()
            c = 0
            while (c == 0):
                if (len(qtty) == 1):
                    if (qtty[0] in numbers):
                        c = 1
                elif (len(qtty) == 2):
                    if (qtty[0] in numbers and qtty[1] in numbers):
                        c = 1
                elif (len(qtty) == 3):
                    if (int(qtty) == 100):
                        c = 1
                else:
                    c = 0
                if (c == 0):
                    print("Некорректное значение")
                    qtty = input()
            p.append(int(qtty))
        matrix.append(p)

    print()
    for i in range(M):  # вывод изначальной матрицы
        for j in range(M):
            print(matrix[i][j], end=" ")
        print()

    for i in range(len(matrix)):  # закидываю элементы выше побочной диагонали
        for j in range(len(matrix) - i):
            tmp.append(matrix[i][j])

    bubble_sort(tmp)  # сортируем элементы

    k = 0
    for i in range(len(matrix)):
        for j in range(len(matrix) - i):
            matrix[i][j] = tmp[k]
            k += 1
            if (k == len(tmp)):
                break

for i in range(M):  # оставшиеся не сортированные элементы умножаю на минус один
    for j in range(M):
        if (i > (M - j - 1)):
            matrix[i][j] = matrix[i][j] * (-1)

print()

for i in range(M):  # вывод конечной матрицы
    for j in range(M):
        print(matrix[i][j], end=" ")
    print()
