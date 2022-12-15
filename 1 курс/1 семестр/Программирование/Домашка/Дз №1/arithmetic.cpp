#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Арифметика
    float a, b;
    cin >> a >> b;
    cout << a + b << endl;
    cout << a - b << endl;
    cout << a * b << endl;
    if (b != 0)
    {
        cout << a / b << endl;
    }
    else
    {
        cout << "На 0 нельзя делить" << endl;
    }

    return 0;
}
