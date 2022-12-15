#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");

    int n(0), m(0), ans(0);
    cin >> n >> m;
    for (int x1 = 0; x1 < n; x1++)
    {
        for (int x2 = x1; x2 < n; x2++)
        {
            for (int y1 = 0; y1 < m; y1++)
            {
                for (int y2 = y1; y2 < m; y2++)
                {
                    ans++;
                }
            }
        }
    }
    cout << ans << endl;

    return 0;
}
