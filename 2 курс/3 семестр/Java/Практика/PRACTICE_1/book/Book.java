package book;
import java.lang.*;
public class Book {
    private String name;
    private String author;
    private int year;

    public Book(String n, String a, int y) {
        name = n;
        author = a;
        year = y;
    }

    public Book(String n, String a) {
        name = n;
        author = a;
        year = 0;
    }

    public Book() {
        name = "Untitled";
        author = "Untitled";
        year = 0;
    }

    public void setYear(int year) {
        this.year = year;
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setAuthor(String author) {
        this.author = author;
    }

    public String getName(String name) {
        return name;
    }
    public String getAuthor(String author) {
        return author;
    }

    public int getYear() {
        return year;
    }

    @Override
    public String toString() {
        return "Название книги: " + this.name + ", Автор книги: " + this.author + ", Год выпуска: " + this.year;
    }
}
