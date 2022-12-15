#include <iostream>
#include <fstream>
#include <string>

using namespace std;

string get_word(istream& is) /// Обработка текстовых файлов (4 и 6)
{
    string w;
    is >> w;
    return w;
}

int main()
{
    setlocale(0, "");
    /// Обработка текстовых файлов (6)
    ifstream file("tmp.txt");
    if (!file.is_open())
    {
        cout << "Ошибка! Файла нет" << endl;
        return 0;
    }

    string word, min_word;
    int min_len = 1000000;

    while (file)
    {
        word = get_word(file);
        if (word.size() == 0)
        {
            break;
        }
        if (word.size() < min_len)
        {
            min_len = word.size();
            min_word = word;
        }
    }

    file.close();

    cout << "Самое короткое слово: " << min_word << endl;

    return 0;
}
