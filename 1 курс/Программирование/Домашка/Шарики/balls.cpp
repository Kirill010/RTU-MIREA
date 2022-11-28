#include <iostream>
#include <string>

using namespace std;

int ans = 0;

void permutations(string s, int i, int n)
{
    if (i == n - 1)
    {
        for (int i = 0; i < n; i++)
        {
            if ((s[i] - '0') == i)
            {
                ans++;
                break;
            }
        }
        return;
    }

    for (int j = i; j < n; j++)
    {
        swap(s[i], s[j]);
        permutations(s, i + 1, n);
        swap(s[i], s[j]);
    }
}

int main()
{
    setlocale(0, "");

    int n(0);
    cin >> n;

    /// string s = "0123456789";
    string s;

    for (int i = 0; i < n; i++)
    {
        s.push_back((char)i + '0');
    }

    permutations(s, 0, s.size());
    cout << "Ответ: " << ans << endl;
    return 0;
}
