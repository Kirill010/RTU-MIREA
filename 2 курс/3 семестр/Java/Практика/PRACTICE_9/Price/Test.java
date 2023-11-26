package Price;

public class Test {
    public static void main(String[] args) {
        Priceable printable = new Guitar(5000);
        System.out.println("Gibson Les Paul стоит: " + printable.getPrice());
        printable = new Home(100000);
        System.out.println("Дом стоит: " + printable.getPrice());
    }
}
