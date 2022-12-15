#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Табуляция
    for (float x = -4; x <= 4; x = x + 0.5)
    {
        if (x == 1)
        {
            continue;
        }
        float y = (((x * x) - (2 * x) + 2) / (x - 1));
        cout << y << endl;
    }

    return 0;
}
