#include <iostream>
#include <vector>

using namespace std;

int main()
{
    setlocale(0, "");

    /// Задача Умножение матриц
    /// m = 3 n = 4 k = 4 p = 2

    cout << "Введите таблицу A: " << endl;
    double a[3][4];
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 4; j++)
        {
            cin >> a[i][j];
        }
    }

    cout << "Введите таблицу B: " << endl;
    double b[4][2];
    for (int i = 0; i < 4; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cin >> b[i][j];
        }
    }

    double c[3][2];

    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            c[i][j] = 0; /// обнуление массива
        }
    }

    for (int i = 0; i < 3; i++)
    {
        /// процесс умножения матриц
        for (int j = 0; j < 2; j++)
        {
            for (int k = 0; k < 4; k++)
            {
                c[i][j] += (a[i][k] * b[k][j]);
            }
        }
    }

    /// вывод матрицы С
    for (int i = 0; i < 3; i++)
    {
        for (int j = 0; j < 2; j++)
        {
            cout << c[i][j] << "\t";
        }
        cout << endl;
    }

    int maxsellermoney(0);
    double maxs1(0);
    for (int i = 0; i < 3; i++)
    {
        double tmp1(0);
        for (int j = 0; j < 2; j++)
        {
            tmp1 += c[i][j];
        }
        if (tmp1 > maxs1)
        {
            maxsellermoney = i; /// номер продавца, который больше всего денег выручил с продажи
            maxs1 = tmp1;
        }
    }

    int minsellermoney(0);
    double mins1(10000000);
    for (int i = 0; i < 3; i++)
    {
        double tmp2(0);
        for (int j = 0; j < 2; j++)
        {
            tmp2 += c[i][j];
        }
        if (tmp2 < mins1)
        {
            minsellermoney = i; /// номер продавца, который меньше всего денег выручил с продажи
            mins1 = tmp2;
        }
    }

    int maxsellercom(0);
    double maxs2(0);
    for (int i = 0; i < 3; i++)
    {
        double tmp3 = c[i][1];
        if (tmp3 > maxs2)
        {
            maxsellercom = i; /// номер продавца, который больше всего получил комиссионных
            maxs2 = tmp3;
        }
    }

    int minsellercom(0);
    double mins2(10000000);
    for (int i = 0; i < 3; i++)
    {
        double tmp4 = c[i][1];
        if (tmp4 < mins2)
        {
            minsellercom = i; /// номер продавца, который меньше всего получил комиссионных
            mins2 = tmp4;
        }
    }


    double allmoney(0), allcom(0), alls(0);
    for (int i = 0; i < 3; i++)
    {
        allmoney += c[i][0];
        allcom += c[i][1];
        alls += (c[i][0] + c[i][1]);
    }

    cout << "1 - " << "Больше у " << maxsellermoney + 1 << " продавца" << endl;
    cout << "1 - " << "Меньше у " << minsellermoney + 1 << " продавца" << endl;
    cout << "2 - " << "Больше у " << maxsellercom + 1 << " продавца" << endl;
    cout << "2 - " << "Меньше у " << minsellercom + 1 << " продавца" << endl;
    cout << "3 - " << "Общая сумма денег: " << allmoney << " вырученных за проданные товары" << endl;
    cout << "4 - " << "Всего комиссионных: " << allcom << " получили продавцы" << endl;
    cout << "5 - " << "Общая сумма денег: " << alls << " прошедших через руки продавцов" << endl;

    return 0;
}
