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
    /// Обработка текстовых файлов (4)
    ifstream file("tmp.txt");
    if (!file.is_open())
    {
        cout << "Ошибка! Файла нет" << endl;
        return 0;
    }

    string word, max_word;
    int max_len = 0;

    while (file)
    {
        word = get_word(file);
        if (word.size() == 0)
        {
            break;
        }
        if (word.size() > max_len)
        {
            max_len = word.size();
            max_word = word;
        }
    }

    file.close();

    cout << "Самое длинное слово: " << max_word << endl;

    return 0;
}
