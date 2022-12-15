#include <iostream>
#include <vector>

using namespace std;

int roman(char x)
{
    switch (x)
    {
        case 'I':
            return 1;
        case 'V':
            return 5;
        case 'X':
            return 10;
        case 'L':
            return 50;
        case 'C':
            return 100;
        case 'D':
            return 500;
        case 'M':
            return 1000;
        default:
            return 0;
            break;
    }
}

int main()
{
    setlocale(0, "");
    /// Задача Автоматный распознаватель
    string s;
    cout << "Введите римскую цифру: ";
    cin >> s;
    vector <char> znak;
    int x = 0, tmp1 = 0;
    for (int i = s.size() - 1; i >= 0; i--)
    {
        int tmp = roman(s[i]);
        if (tmp >= tmp1)
        {
            tmp1 = tmp;
        }
        if (tmp == tmp1)
        {
            x += tmp;
            znak.push_back('1');
        }
        else
        {
            znak.push_back('0');
            x -= tmp;
        }
    }
    bool flag = 1;
    if (znak.size() > 2)
    {
        for (int j = 1; j < znak.size() - 1; j++)
        {
            if (znak[j - 1] == '1' and znak[j] == '0' and znak[j + 1] == '0')
            {
                flag = 0;
            }
            if (flag == 0)
            {
                cout << "Ошибка" << endl;
            }
            else
            {
                cout << x << endl;
                for (int k = 0; k < znak.size(); k++)
                {
                    /// cout << znak[k] << " ";
                }
            }
        }
    }
    else
    {
        cout << x << endl;
    }

    return 0;
}
