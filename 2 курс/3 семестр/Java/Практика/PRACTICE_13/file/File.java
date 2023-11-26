package file;

import java.io.*;

import java.io.FileReader;
import java.io.FileWriter;
import java.io.IOException;
import java.util.Scanner;

public class File {
    public void t_1(String name) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Введите текст: ");
        String text = sc.nextLine();
        try(FileWriter writer = new FileWriter(name, false))
        {
            writer.append(text);
            writer.flush();
        }
        catch(IOException ex) {

            System.out.println(ex.getMessage());
        }
    }
    public void t_2(String name) {
        try(FileReader reader = new FileReader(name))
        {
            // читаем посимвольно
            int c;
            while((c=reader.read())!=-1){
                System.out.print((char)c);
            }
        }
        catch(IOException ex){

            System.out.println(ex.getMessage());
        }
    }
    public void t_4(String name) {
        try(FileWriter writer = new FileWriter(name, true))
        {
            Scanner sc = new Scanner(System.in);
            System.out.println("Введите текст: ");
            String text = sc.nextLine();
            writer.append('\n');
            writer.append(text);
            writer.flush();
        }
        catch(IOException ex) {

            System.out.println(ex.getMessage());
        }
    }

}