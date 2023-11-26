package ru.mirea.lab1;

import java.util.Scanner;
public class array_1
{
    public static void main(String[] args)
    {

        Scanner in = new Scanner(System.in);
        int num = in.nextInt();

        double a = 0;

        int[] arr = new int[num];

        for (int i = 0; i < num; i++)
        {
            arr[i] = in.nextInt();
            a += arr[i];
        }
        System.out.println(a);
        double ans = a / num;

        System.out.println(ans);
    }
}
