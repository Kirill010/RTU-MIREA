#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Конус
    double R, r, h;
    cout << "Введите радиус основания R" << endl;
    cin >> R;
    cout << "Введите радиус верхнего основания r" << endl;
    cin >> r;
    cout << "Введите высоту h" << endl;
    cin >> h;
    if (R >= 0 and r >= 0 and h >= 0)
    {
        double l = sqrt(((R - r) * (R - r)) + (h * h));
        double pi = 3.14;
        double V = (pi * h * ((R * R) + (R * r) + (r * r))) / 3;
        double S = pi * ((R * R) + ((R + r) * l) + (r * r));
        cout << V << " " << S << endl;
    }
    else
    {
        cout << "Есть отрицательные цифры." << endl;
    }
    
    return 0;
}
