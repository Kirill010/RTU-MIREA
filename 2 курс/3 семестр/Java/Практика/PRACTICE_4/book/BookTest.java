package book;

import circle.Circle;

public class BookTest {
    public static void main(String[] args) {
        Book b1 = new Book("Преступление и наказание", "Ф.М.Достоевский", 1865);
        System.out.println(b1);
        b1.setYear(1866);
        System.out.println(b1);
    }
}
