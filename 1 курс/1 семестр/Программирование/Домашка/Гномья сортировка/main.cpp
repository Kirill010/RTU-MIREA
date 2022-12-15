#include <iostream>

using namespace std;

void gnomesort(int arr[], int n)
{
    int index(0);

    while (index < n)
    {
        if (index == 0 or arr[index] > arr[index - 1])
        {
            index++;
        }
        else
        {
            swap(arr[index], arr[index - 1]);
            index--;
        }
    }
    return;
}

void printArray(int arr[], int n)
{
    cout << "Отсортированный массив: ";
    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
    }
    cout << endl;
}

int main()
{
    setlocale(0, "");

    /// Задали элементы массива
    int arr[] = {78, 43, 256, -362, 2463, 362, 34, -351, 35, -832, 4, 6, -24, 57};

    /// Вычисляем количество элементов (размер массива в байтах / один элемент массива в байтах)
    int n = sizeof(arr) / sizeof(arr[0]); /// sizeof() возвращает количество байт

    gnomesort(arr, n);
    printArray(arr, n);

    return 0;
}
