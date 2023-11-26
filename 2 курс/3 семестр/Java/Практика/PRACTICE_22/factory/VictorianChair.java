package factory;

public class VictorianChair implements Chair {
    private int age;

    public int getAge() {
        return age;
    }

    @Override
    public void sitOn() {
        System.out.println("Вы сидите на Викторианском стуле возрастом" + getAge());
    }
}
