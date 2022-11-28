#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Уравнение
    float b, c;
    cin >> b >> c;
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

    return 0;
}
