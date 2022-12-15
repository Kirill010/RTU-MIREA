#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");

    int n, k;
    cin >> n >> k;
    while (k != 1)
    {
        n = (n - k % 2) / 2;
        k /= 2;
    }
    cout << (n - 1) / 2 << endl;
    cout << n / 2 << endl;

    return 0;
}
