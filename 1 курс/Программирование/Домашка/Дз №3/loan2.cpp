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
    /// Задача Ссуда
    double S, m, n;
    cout << "Введите S рублей" << endl;
    cin >> S;
    cout << "Введите m месячной выплаты" << endl;
    cin >> m;
    cout << "Введите n лет" << endl;
    cin >> n;
    for (double p = 1; p < 100; p++)
    {
        double r, m1;
        r = p / 100;
        m1 = (S * r * pow((1 + r), n)) / (12 * (pow((1 + r), n) - 1));
        if (m1 >= m)
        {
            cout << "Процент =  " << p << endl;
            break;
        }
    }
    
    return 0;
}
