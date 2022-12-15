#include <iostream>
#include <fstream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Файл
    ofstream ofile("1.txt");
    if (!ofile.is_open())
    {
        cout << "Ошибка! Файла нет" << endl;
    }

    for (int i = 1; i <= 10; i++)
    {
        float x;
        cout << "Введите " << i << " число: ";
        cin >> x;
        ofile << x << '\n';
    }
    ofile.close();

    ifstream ifile("1.txt");
    if (!ifile.is_open())
    {
        cout << "Ошибка! Файла нет" << endl;
    }

    float sum(0);
    for (int i = 0; i < 10; i++)
    {
        float x1;
        ifile >> x1;
        sum += x1;
    }
    ifile.close();

    cout << "Сумма чисел = " << sum << endl;

    return 0;
}
