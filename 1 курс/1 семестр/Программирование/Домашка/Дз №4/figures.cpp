#include <iostream>
#include <cmath>

using namespace std;

void square(float a, float b) /// Прямоугольник
{
    if (a > 0 and b > 0)
    {
        cout << "Площадь прямоугольника: " << a * b << endl;
    }
    else
    {
        cout << "Числа должны быть больше 0" << endl;
    }
}

void triangle(float a, float b, float c) /// Треугольник
{
    if ((a > 0 and b > 0 and c > 0) and ((a + b > c and a + c > b and c + b > a)))
    {
        float p = (a + b + c) / 2;
        cout << "Площадь треугольника: " << sqrt(p * (p - a) * (p - b) * (p - c)) << endl;
    }
    else
    {
        cout << "Некорректные значения" << endl;
    }
}

void circle(float r) /// Круг
{
    if (r > 0)
    {
        float pi = 3.14;
        cout << "Площадь круга: " << pi * r * r << endl;
    }
    else
    {
        cout << "Числа должны быть больше 0" << endl;
    }
}

int main()
{
    setlocale(0, "");
    /// Задача Геометрические фигуры
    cout << "Какую площадь хотите узнать: прямоугольник - 1, треугольник - 2, круг - 3" << endl;
    int menu(0);
    cin >> menu;
    if (menu == 1)
    {
        float a, b;
        cout << "Введите значения для прямоугольника: a и b" << endl;
        cin >> a >> b;
        square(a, b);
    }
    else if (menu == 2)
    {
        float a1, b1, c1;
        cout << "Введите значения для треугольника: a1, b1, c1" << endl;
        cin >> a1 >> b1 >> c1;
        triangle(a1, b1, c1);
    }
    else if (menu == 3)
    {
        float r;
        cout << "Введите значения для круга: r" << endl;
        cin >> r;
        circle(r);
    }
    else
    {
        cout << "Ошибка" << endl;
    }


    return 0;
}
