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
    /// Задача Заем
    double S, p, n;
    cout << "Введите S рублей" << endl;
    cin >> S;
    cout << "Введите p процент" << endl;
    cin >> p;
    cout << "Введите n лет" << endl;
    cin >> n;
    if (S > 0 and p > 0 and n > 0)
    {
        double r = p / 100;
        float m = (S * r * pow((1 + r), n)) / (12 * (pow((1 + r), n) - 1));
        cout << m << endl;
    }
    else
    {
        cout << "Вы ввели некорректные цифры" << endl;
    }

    return 0;
}
