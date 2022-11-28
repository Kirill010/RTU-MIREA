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
    /// Задача Копирование файла
    string x;

    cout << "Введите что-нибудь" << endl;
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
    while (!ifile.eof())
    {
        getline(ifile, y);
        cout << "Содержимое файла: " << y << endl;
    }

    ifile.close();
    
    return 0;
}
