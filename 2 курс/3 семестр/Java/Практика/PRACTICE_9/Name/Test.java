package Name;

public class Test {
    public static void main(String[] args) {
        Nameable printable = new Planet("Земля");
        System.out.println("Планета: " + printable.getName());
        printable = new Cars("Lexus");
        System.out.println("Марка автомобиля: " + printable.getName());
    }
}
