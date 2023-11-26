package ball;

public class TestBall {
    public static void main(String[] args) {
        Ball b1 = new Ball("Футбольный", "латекс");
        System.out.println(b1);
        b1.setName("Баскетбольный");
        b1.setmaterial("кожа");
        System.out.println(b1);
    }
}
