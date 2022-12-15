#include <iostream>
#include <cmath>

using namespace std;

int fact(int n) /// Ряды (3)
{
    int p = 1;
    for (int i = 1; i <= n; i++)
    {
        p *= i;
    }
    return p;
}

int main()
{
    setlocale(0, "");
    /// Задача Ряды (3)
    int n(0), tmp = 2;
    float y, ans = 1;
    float sum = sin(2);
    cout << "Введите число n:" << endl;
    cin >> n;
    for (int i = 1; i <= n; i++)
    {
        y = fact(i) / sum;
        tmp += 2;
        sum += sin(tmp);
        ans *= y;
    }
    cout << ans << endl;

    return 0;
}
