#include <iostream>

using namespace std;

void sign(float x)
{
    if (x > 0)
    {
        cout << "1" << endl;
    }
    else if (x == 0)
    {
        cout << "0" << endl;
    }
    else
    {
        cout << "-1" << endl;
    }
}

int main()
{
    setlocale(0, "");
    /// Задача Знак числа
    float x(0);
    cin >> x;
    sign(x);

    return 0;
}
