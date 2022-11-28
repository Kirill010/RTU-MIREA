#include <iostream>
#include <vector>

using namespace std;

int main()
{
    setlocale(0, "");

    int n(0);
    vector <int> coupe(9, 0);
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        int tmp(0);
        cin >> tmp;
        if ((tmp >= 1 and tmp <= 4) or tmp == 53 or tmp == 54)
        {
            coupe[0]++;
        }
        else if ((tmp >= 5 and tmp <= 8) or tmp == 51 or tmp == 52)
        {
            coupe[1]++;
        }
        else if ((tmp >= 9 and tmp <= 12) or tmp == 49 or tmp == 50)
        {
            coupe[2]++;
        }
        else if ((tmp >= 13 and tmp <= 16) or tmp == 47 or tmp == 48)
        {
            coupe[3]++;
        }
        else if ((tmp >= 17 and tmp <= 20) or tmp == 45 or tmp == 46)
        {
            coupe[4]++;
        }
        else if ((tmp >= 21 and tmp <= 24) or tmp == 43 or tmp == 44)
        {
            coupe[5]++;
        }
        else if ((tmp >= 25 and tmp <= 28) or tmp == 41 or tmp == 42)
        {
            coupe[6]++;
        }
        else if ((tmp >= 29 and tmp <= 32) or tmp == 39 or tmp == 40)
        {
            coupe[7]++;
        }
        else if ((tmp >= 33 and tmp <= 36) or tmp == 37 or tmp == 38)
        {
            coupe[8]++;
        }
    }

    int c(0), max_count(0);
    for (int i = 0; i < 9; i++)
    {
        if (coupe[i] == 6)
        {
            c++;
        }
        if (c > max_count)
        {
            max_count = c;
        }
        else
        {
            c = 0;
        }
    }

    cout << max_count << endl;

    return 0;
}
