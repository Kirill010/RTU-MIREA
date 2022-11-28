#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");

    int m(0);
    cin >> m;
    int l3(0), l4(0);
    l4 = m % 3;
    l3 = (m - 4 * l4) / 3;
    if (l3 >= 0)
    {
        cout << l3 << endl;
        cout << l4 << endl;
    }
    else
    {
        cout << 0 << endl;
        cout << 0 << endl;
    }

    return 0;
}
