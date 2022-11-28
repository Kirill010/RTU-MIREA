#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Файлы (8)
    cout << "Введите порядок: ";
    float n(0);
    cin >> n;
    vector<vector<float>> a(n, vector <float>(n));
    vector<vector<float>> b(n, vector <float>(n));
    vector<vector<float>> c(n, vector <float>(n));
    vector<vector<float>> e(n, vector <float>(n));
    vector<vector<float>> m(n, vector <float>(n));


    ofstream file1("old.txt");
    if (!file1.is_open())
    {
        cout << "Ошибка! Файла нет" << endl;
    }

    cout << "Введите элементы матрицы A:" << endl;
    file1 << "Матрица A:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> a[i][j];
            file1 << a[i][j] << " ";
        }
        file1 << endl;
    }

    file1 << endl;

    cout << "Введите элементы матрицы B:" << endl;
    file1 << "Матрица B:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cin >> b[i][j];
            file1 << b[i][j] << " ";
        }
        file1 << endl;
    }

    file1 << endl;

    cout << "Заполняем матрицу E:" << endl;
    file1 << "Матрица E:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            if (i == j)
            {
                e[i][j] = 1;
                file1 << e[i][j] << " ";
            }
            else
            {
                e[i][j] = 0;
                file1 << e[i][j] << " ";
            }
        }
        file1 << endl;
    }

    file1 << endl;

    cout << "Заполняем матрицу C:" << endl;
    file1 << "Матрица C:" << endl;
    for (int i = 1; i <= n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            c[i - 1][j - 1] = (float)1 / (i + j);
            file1 << c[i - 1][j - 1] << " ";
        }
        file1 << endl;
    }

    file1 << endl;

    cout << "Заполняем матрицу M:" << endl;
    file1 << "Матрица M:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            m[i][j] = a[i][j] * (b[i][j] - e[i][j]) + c[i][j];
            file1 << m[i][j] << " ";
        }
        file1 << endl;
    }

    cout << endl;

    cout << "Итог:" << endl;

    cout << "Выводим матрицу A:" << endl;
    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << a[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    cout << "Выводим матрицу B:" << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << b[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    cout << "Выводим матрицу E:" << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << e[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    cout << "Выводим матрицу C:" << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << c[i][j] << " ";
        }
        cout << endl;
    }
    cout << endl;

    cout << "Выводим матрицу M:" << endl;

    for (int i = 0; i < n; i++)
    {
        for (int j = 0; j < n; j++)
        {
            cout << m[i][j] << " ";
        }
        cout << endl;
    }

    cout << endl;

    return 0;
}
