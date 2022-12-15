#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Алгоритм Евклида 2 способ
    int a, b;
    cout << "Введите a: " << endl;
    cin >> a;
    cout << "Введите b: " << endl;
    cin >> b;
    while (b > 0)
    {
        int c = a % b;
        a = b;
        b = c;
    }
    cout << a << endl;

    return 0;
}
