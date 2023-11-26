package book;

public class Book {
    private String author;
    private String name;
    private int year;

    public Book(String a, String n, int y) {
        author = a;
        name = n;
        year = y;
    }

    public Book(String a, String n) {
        author = a;
        name = n;
        year = 0;
    }

    public Book() {
        author = "Untitled";
        name = "Untitled";
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
        return "Автор книги: " + this.author + ", Название книги: " + this.name + ", Год выпуска: " + this.year;
    }
}
