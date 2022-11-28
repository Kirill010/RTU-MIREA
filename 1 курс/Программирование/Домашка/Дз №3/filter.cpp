#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Фильтр
    string x;
    cout << "Введите любые буквы и цифры" << endl;
    getline(cin, x);
    ofstream ofile("tmp.txt");
    if (!ofile.is_open())
    {
        cout << "Ошибка! Файла нет" << endl;
    }

    ofile << x;
    ofile.close();

    ifstream ifile("tmp.txt");
    string y;
    getline(ifile, y);

    ifile.close();

    for (int i = 0; i < y.size(); i++)
    {
        if (isdigit(y[i]))
        {
            cout << y[i];
            while (isdigit(y[i + 1]))
            {
                i++;
                cout << y[i];
            }
            cout << " ";
        }
    }

    return 0;
}
