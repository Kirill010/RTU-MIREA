#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Ряды (1)
    int n(0), tmp = 2;
    double y, ans = 0;
    double sum = sin(1);
    cout << "Введите число n:" << endl;
    cin >> n;
    for (double i = 1; i <= n; i++)
    {
        y = i / sum;
        sum += sin(tmp);
        tmp++;
        ans += y;
    }
    cout << ans << endl;

    return 0;
}
