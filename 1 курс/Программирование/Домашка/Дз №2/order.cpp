#include <iostream>

using namespace std;

int main()
{
    setlocale(0, "");
    /// Задача Порядок
    int N, i(0);
    cin >> N;
    if (N > 0)
    {
        while (i != 10)
        {
            cout << N << " ";
            N++;
            i++;
        }
    }
    else
    {
        cout << "Число не натуральное" << endl;
    }
    
    return 0;
}
