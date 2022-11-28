#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    int n(0), k(0), P(0);
    cout << "Введите количество ступеней: ";
    cin >> n;
    cout << "Введите количество орехов: ";
    cin >> k;
    cout << "Введите прочность ореха: ";
    cin >> P;
    int steps[n];
    for (int i = 0; i < n; i++)
    {
        steps[i] = (i + 1);
    }

    int l = 0;
    int r = (n - 1);
    int cnt(0); /// количество попыток

    while (((r - l) > 1) or (k > 0))
    {
        int mid = (r + l) / 2;
        if (mid < P)
        {
            l = mid;
            k--;
        }
        else
        {
            r = mid;
            k--;
        }
        cnt++;
    }

    if (k > 0)
    {
        cout << "Количество попыток, за которое обезьяна гарантировано сможет определить прочность орехов: " << cnt << endl;
    }
    else
    {
        cout << "Орехи кончились у обезьяны" << endl;
    }

    return 0;
}
