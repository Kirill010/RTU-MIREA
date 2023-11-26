package ru.mirea.lab1;

public class arguments_3
{
    public static void main(String[] args)
    {
        System.out.println("Hello, World!");
        for (int i = 1; i <= args.length; i++)
        {
            System.out.println("Аргумент №" + i + " - " + args[i]);
        }
        // C:\Program Files\Java\jdk-20\bin\
        // java -Dfile.encoding=UTF-8 C:\Users\super\IdeaProjects\MIREA\practice_1\src\ru\mirea\lab1\arguments_3.java test hi me test2
    }
}
