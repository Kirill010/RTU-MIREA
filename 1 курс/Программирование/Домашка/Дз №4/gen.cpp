#include <iostream>

using namespace std;

int g(int const& m, int const& b, int const& c, int const& i) /// Генератор псевдослучайных чисел
{
    if (i == 0)
    {
        return 0;
    }

    return (m * g(m, b, c, i - 1) + b) % c;
}

int main()
{
    setlocale(0, "");
    /// Задача Генератор псевдослучайных чисел
    int m = 37, b = 3, c = 64, i;
    cout << "Введите i: ";
    cin >> i;
    cout << "Число = " << g(m, b, c, i) << endl;

    return 0;
}
