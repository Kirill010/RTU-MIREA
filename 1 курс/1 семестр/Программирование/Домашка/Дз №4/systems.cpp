#include <iostream>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Системы счисления
    string number;
    cout << "Введите число: ";
    cin >> number;
    cout << "Введите основание числа: ";
    int base(0);
    cin >> base;
    cout << "Введите основание, в которую хотите перевести: ";
    int new_base(0);
    cin >> new_base;
    int number_10(0);
    for (int i = 0; i < number.size(); i++)
    {
        char s = number[i];
        int n(0);
        if (isdigit(s))
        {
            n = s - '0';
        }
        else
        {
            n = s - 'A' + 10;
        }

        if (n >= base)
        {
            cout << "Ошибка!" << endl;
            return 0;
        }

        number_10 += n * int(pow(base, number.size() - 1 - i));
    }

    string new_number;
    while (number_10 > 0)
    {
        int ost = number_10 % new_base;
        string c;
        if (ost > 9)
        {
            c = 'A' + ost - 10;
        }
        else
        {
            c = to_string(ost);
        }
        new_number += c;

        number_10 /= new_base;
    }

    reverse(new_number.begin(), new_number.end());
    if (new_number.size() == 0)
    {
        cout << 0 << endl;
    }
    else
    {
        cout << "Ответ: " << new_number << endl;
    }

    return 0;
}
