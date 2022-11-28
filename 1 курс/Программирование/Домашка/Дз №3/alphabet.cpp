#include <iostream>
#include <cmath>
#include <fstream>
#include <string>
#include <algorithm>
#include <vector>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Сортировка букв (сортировка пузырьком)
    cout << "Введите 30 букв" << endl;
    string alpha;
    cin >> alpha;
    if (alpha.size() >= 30)
    {
        alpha = alpha.substr(0, 30);
        for (int i = 0; i < 30; i++)
        {
            for (int j = 0; j < 30 - (i + 1); j++)
            {
                if (alpha[j] > alpha[j + 1])
                {
                    char b;
                    b = alpha[j];
                    alpha[j] = alpha[j + 1];
                    alpha[j + 1] = b;
                }
            }
        }
        cout << "Массив в отсортированном виде: " << endl;
        for (int i = 0; i < 30; i++)
        {
            cout << alpha[i] << " ";
        }
    }
    else
    {
        cout << "Вы ввели меньше 30 символов!" << endl;
    }

    return 0;
}
