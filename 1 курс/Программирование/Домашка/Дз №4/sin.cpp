#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Синусоида
    char s[100][200];
    for (int i = 0; i < 40; i++)
    {
        for (int j = 0; j < 120; j++)
        {
            s[i][j] = '=';
        }
    }

    for (int i = 0; i < 120; i++)
    {
        s[40 / 2][i] = '-';
    }

    for (int i = 0; i < 40; i++)
    {
        s[i][120 / 2 - 2] = '|';
    }

    int y;
    for (int i = -120 / 2; i < 120 / 2; i++)
    {
        if (i == 0 or i == -31 or i == 31 or i == 1)
        {
            continue;
        }
        int b(0);
        if (i > -31)
        {
            b = 1;
        }
        if (i > 0)
        {
            b = 3;
        }
        if (i > 31)
        {
            b = 4;
        }
        y = sin((float) i / 10) * 10;
        s[y + 40 / 2][i + 120 / 2 - b] = '0';
    }

    for (int i = 0; i < 40; i++)
    {
        for (int j = 0; j < 120; j++)
        {
            cout << s[i][j];
        }
        cout << endl;
    }

    return 0;
}
