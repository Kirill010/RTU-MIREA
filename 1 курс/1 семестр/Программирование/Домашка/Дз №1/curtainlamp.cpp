#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Лампа со шторой
    bool day, shtori, lamp;
    cout << "Если ночь пишем 0, если день пишем 1" << endl;
    cin >> day;
    cout << "Если не раздвинуты шторы пишем 0, если раздвинуты шторы пишем 1" << endl;
    cin >> shtori;
    cout << "Если выключена лампа пишем 0, если включена лампа пишем 1" << endl;
    cin >> lamp;
    if ((day == 1 and shtori == 1) or (lamp == 1))
    {
        cout << "В комнате светло" << endl;
    }
    else
    {
        cout << "В комнате не светло" << endl;
    }

    return 0;
}
