package ru.mirea.lab1;

import java.util.Scanner;

public class factorial_5
{

    public static void main(String[] args)
    {
        while (true)
        {
            System.out.println("Введи число больше 0 и меньше 20!");
            Scanner in = new Scanner(System.in);
            long num = in.nextInt();
            if (num < 0)
            {
                System.out.println("Введи число больше 0!");
            }
            else if (num > 20)
            {
                System.out.println("Введи другое меньше 20!");
            }
            else
            {
                long prod = 1;
                for (int i = 1; i <= num; i++)
                {
                    prod *= i;
                }
                System.out.println(prod);
                break;
            }
        }
    }
}
