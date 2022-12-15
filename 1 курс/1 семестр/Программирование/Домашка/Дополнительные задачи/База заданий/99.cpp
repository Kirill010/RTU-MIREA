#include <iostream>
#include <random>
#include <ctime>
#include <string>

using namespace std;

int random_num(0);

int main()
{
    setlocale(0, "");
    int tmp = rand() % 999 + 1000; /// комп задумывает число
    string st = to_string(tmp); /// переводим в строку
    do
    {
        int tmp = rand() % 999 + 1000;
        string st = to_string(tmp);
        random_num = tmp;
    } /// проверяем, чтобы все цифры были разные
    while (st[0] != st[1] and st[0] != st[2] and st[0] != st[3] and st[1] != st[2] and st[1] != st[3] and st[2] != st[3]);
    /// cout << random_num << endl;
    string s;
    s = to_string(random_num);
    /// начинаем игру
    cout << "ИИ задумал число, попытайтесь его отгадать (это число четырёхзначное)" << endl;
    while (true)
    {
        int bulls(0), cows(0);
        string qtty;
        cin >> qtty;
        for (int i = 0; i < s.size(); i++)
        {
            if (s[i] == qtty[i])
            {
                bulls++;
            }
        }
        for (int i = 0; i < s.size(); i++)
        {
            if ((s[i] != qtty[i]) and (qtty.find(s[i]) != string::npos))
            {
                cows++;
            }
        }
        if (bulls == 4)
        {
            cout << "4 плюса. Вы победили!" << endl;
            return 0;
        }
        cout << bulls << " плюс(а) и " << cows << " минус(а)" << endl;
    }
    
    return 0;
}
