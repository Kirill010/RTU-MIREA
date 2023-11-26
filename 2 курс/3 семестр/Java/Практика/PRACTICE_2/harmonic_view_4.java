package ru.mirea.lab1;

import java.util.Scanner;

public class harmonic_view_4
{
    public static void main(String[] args)
    {
        Scanner in = new Scanner(System.in);
        int num = 10;
        double n = 0;
        for (int i = 1; i <= num; i++)
        {
            n += (double) 1 / i;

            System.out.println(i + " знаменатель = " + n);
        }
        System.out.println(n);
    }
}
