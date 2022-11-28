#include <iostream>
#include <string>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Былая слава
    cout << "Былая слава 1912 года" << endl;
    cout << endl;
    string mas[6][40];
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 40; j++)
        {
            if (i < 6)
            {
                if (i % 2 == 0 and j < 8)
                {
                    mas[i][j] = "* ";
                }
                if (i % 2 == 1 and j < 8)
                {
                    mas[i][j] = "* ";
                }
                if (i % 2 == 0 and j > 8)
                {
                    mas[i][j] = "-";
                }
                if (i % 2 == 1 and j > 8)
                {
                    mas[i][j] = "-";
                }
            }
            cout << mas[i][j];
        }
        cout << endl;
    }

    string mas1[6][47];
    for (int i = 0; i < 6; i++)
    {
        for (int j = 0; j < 47; j++)
        {
            mas1[i][j] = "-";
            cout << mas1[i][j];
        }
        cout << endl;
    }

    return 0;
}
