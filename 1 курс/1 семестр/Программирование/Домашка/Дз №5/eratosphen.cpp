#include <iostream>
#include <vector>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Алгоритм Эратосфена
    int n;
    cout << "Введите натуральное число: " << endl;
    cin >> n;
    if (n < 1)
    {
        cout << "Число должно быть больше 1!" << endl;
    }
    vector <int> a;
    for (int i = 0; i <= n; i++)
    {
        a.push_back(i);
    }
    int i = 2;
    while (i < (n - 1))
    {
        if (a[i] != 0)
        {
            for (int j = (i * 2); j < n; j += i)
            {
                a[j] = 0;
            }
        }
        i++;
    }
    vector <int> prosto;
    for (int i = 0; i < a.size(); i++)
    {
        if (a[i] != 0 and a[i] >= 2)
        {
            prosto.push_back(a[i]);
        }
    }
    if (prosto.size() == 1)
    {
        cout << prosto[0] << endl;
    }
    else
    {
        prosto.pop_back();
        for (int i = 0; i < prosto.size(); i++)
        {
            cout << prosto[i] << " ";
        }
    }

    return 0;
}
