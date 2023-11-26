package mirea.lab2_1;
import java.lang.*;

public class TestAuthor
{
    public static void main(String[] args)
    {
        Author test = new Author("Kirill", "noobmaster6969@ya.ru", 'm');
        System.out.println("Старый email");
        System.out.println(test.toString());
        System.out.println("Новый email");
        test.setEmail("sss@wer.wer");
        System.out.println(test.toString());
    }
}
