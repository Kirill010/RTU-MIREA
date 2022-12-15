#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");

    int a, b, c;
    cin >> a >> b >> c;
    int n = 0;
    while (a + b * n <= c)
    {
        n++;
    }
    cout << n - 1 << endl;

    return 0;
}
