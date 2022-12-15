#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Разветвление
    float x, a;
    cout << "Введите x" << endl;
    cin >> x;
    cout << "Введите a" << endl;
    cin >> a;
    if (abs(x) < 1 and x > 0)
    {
        float w = a * log(abs(x));
        cout << w << endl;
    }
    else if (abs(x) >= 1 and (a - (x * x)) >= 0)
    {
        float w1 = sqrt(a - (x * x));
        cout << w1 << endl;
    }
    else
    {
        cout << "Ограничения!!!!" << endl;
    }
    
    return 0;
}
