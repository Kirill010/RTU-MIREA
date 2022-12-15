#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Функция
    float x, y, b;
    cin >> x >> y >> b;
    if ((b - y) > 0 and (b - x) >= 0)
    {
        float z = log(b - y) * sqrt(b - x);
        cout << z << endl;
    }
    else
    {
        cout << "Ограничения!!!!" << endl;
    }
    
    return 0;
}
