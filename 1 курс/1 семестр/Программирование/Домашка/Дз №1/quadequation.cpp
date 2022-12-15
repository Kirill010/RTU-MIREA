#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Ещё уравнение
    float a, b, c;
    cin >> a >> b >> c;
    if (a == 0)
    {
        if (b == 0 and c == 0)
        {
            cout << "x - любое число" << endl;
        }
        else if (b == 0 and c != 0)
        {
            cout << "Нет корней" << endl;
        }
        else
        {
            float x = -c / b;
            cout << x << endl;
        }
    }
    else
    {
        float discriminant = ((pow(b, 2)) - (4 * a * c));
        if (discriminant > 0)
        {
            float x1 = ((-b + sqrt(discriminant)) / (2 * a));
            float x2 = ((-b - sqrt(discriminant)) / (2 * a));
            cout << x1 << " " << x2 << endl;
        }
        else if (discriminant == 0)
        {
            float x = -b / (2 * a);
            cout << x << endl;
        }
        else
        {
            cout << "Нет корней" << endl;
        }
    }

    return 0;
}
