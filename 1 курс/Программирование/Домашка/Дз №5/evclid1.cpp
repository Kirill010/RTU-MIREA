#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Алгоритм Евклида 1 способ
    int a, b;
    cout << "Введите a: " << endl;
    cin >> a;
    cout << "Введите b: " << endl;
    cin >> b;
    if (a == 0)
    {
        cout << b << endl;
    }
    else if (b == 0)
    {
        cout << a << endl;
    }
    else if (a == 0 and b == 0)
    {
        cout << "Неопределённость" << endl;
    }
    else
    {
        while (a != b)
        {
            if (a > b)
            {
                a -= b;
            }
            else
            {
                b -= a;
            }
        }
        cout << a << endl;
    }

    return 0;
}
