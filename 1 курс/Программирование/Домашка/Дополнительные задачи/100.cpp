#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

int main()
{
    setlocale(0, "");
    int n(0), k(0);
    cout << "Введите количество поколений: ";
    cin >> n;
    cout << "Введите размер поля: ";
    cin >> k;
    vector<vector<char> > tmp(k, vector<char>(k));
    vector<vector<int> > present(k, vector<int>(k, 0));
    vector<vector<int> > future(k, vector<int>(k, 0));

    ifstream fin("work_data.txt");
    if (!fin.is_open()) /// если файл не открыт
    {
        cout << "Файл не может быть открыт!" << endl;
    }
    else
    {
        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                fin >> tmp[i][j];
            }
        }
        fin.close(); /// закрываем файл
    }

    cout << endl;

    n--; /// минус одно полоколение

    for (int i = 0; i < k; i++)
    {
        for (int j = 0; j < k; j++)
        {
            if (tmp[i][j] == 'X')
            {
                present[i][j] = 1;
                future[i][j] = 1;
            }
            else if (tmp[i][j] == '-')
            {
                present[i][j] = 0;
                future[i][j] = 0;
            }
        }
    }

    /// записываем поколения в файл present
    ofstream fout("work_out.txt");
    if (!fout.is_open()) /// если файл не открыт
    {
        cout << "Файл не может быть открыт!" << endl;
    }
    else
    {
        fout << "--------------------\n";
        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                fout << present[i][j];
            }
            fout << "\n";
        }
        fout.close(); /// закрываем файл
    }

    /// теперь работаем с массивом future
    while (n != 0)
    {

        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                int cnt = 0;
                if (i + 1 < k and present[i + 1][j] != 0)
                {
                    cnt++; /// вниз
                }

                if (i - 1 >= 0 and present[i - 1][j] != 0)
                {
                    cnt++; /// вверх
                }

                if (j + 1 < k and present[i][j + 1] != 0)
                {
                    cnt++; /// вправо
                }

                if (j - 1 >= 0 and present[i][j - 1] != 0)
                {
                    cnt++; /// влево
                }

                if (i + 1 < k and j + 1 < k and present[i + 1][j + 1] != 0)
                {
                    cnt++; /// нижний правый
                }

                if (i - 1 >= 0 and j + 1 < k and present[i - 1][j + 1] != 0)
                {
                    cnt++; /// верхний правый
                }

                if (i + 1 < k and j - 1 >= 0 and present[i + 1][j - 1] != 0)
                {
                    cnt++; /// нижний левый
                }

                if (i - 1 >= 0 and j - 1 >= 0 and present[i - 1][j - 1] != 0)
                {
                    cnt++; /// верхний левый
                }

                if (cnt == 2 or cnt == 3)
                {
                    future[i][j]++;
                }

                else
                {
                    future[i][j] = 0;
                }

                if ((cnt == 12))
                {
                    future[i][j] = 0;
                }
            }
        }

        fstream fout1("work_out.txt", ios::app);
        if (!fout1.is_open()) /// если файл не открыт
        {
            cout << "Файл не может быть открыт!" << endl;
        }
        else
        {
            fout1 << "--------------------\n";
            for (int i = 0; i < k; i++)
            {
                for (int j = 0; j < k; j++)
                {
                    fout1 << future[i][j];
                }
                fout1 << "\n";
            }
            fout1.close(); /// закрываем файл
        }

        for (int i = 0; i < k; i++)
        {
            for (int j = 0; j < k; j++)
            {
                present[i][j] = future[i][j];
            }
        }
        n--; /// минус одно полоколение
    }
    return 0;
}
