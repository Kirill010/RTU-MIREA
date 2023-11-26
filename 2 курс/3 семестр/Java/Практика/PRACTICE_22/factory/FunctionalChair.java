package factory;

public class FunctionalChair implements Chair {

    public int sum(int a, int b) {
        return a + b;
    }

    @Override
    public void sitOn() {
        System.out.println("Вы сидите на Многофункциональном стуле");
    }
}
