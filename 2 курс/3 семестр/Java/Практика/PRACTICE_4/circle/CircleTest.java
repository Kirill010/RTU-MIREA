package circle;

public class CircleTest {
    public static void main(String[] args) {
        Circle c = new Circle(5);
        System.out.println("S = " + c.getArea());
        System.out.println("P = " + c.getPerimeter());
        System.out.println(c.toString());
        c.setRadius(10);
        System.out.println("Новый радиус: " + c.getRadius());
        System.out.println("S = " + c.getArea());
        System.out.println("P = " + c.getPerimeter());
    }
}
