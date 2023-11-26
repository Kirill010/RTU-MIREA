package book;

public class TestBook {
    public static void main(String[] args) {
        Book b1 = new Book("Преступление и наказание", "Ф.М.Достоевский", 1866);
        Book b2 = new Book("1984", "Джордж Оруэлл", 1949);
        Book b3 = new Book("Игра престолов", "Джордж Р.Р. Мартин");
        b3.setYear(1996);
        System.out.println(b1);
        System.out.println(b2);
        System.out.println(b3);
    }
}
