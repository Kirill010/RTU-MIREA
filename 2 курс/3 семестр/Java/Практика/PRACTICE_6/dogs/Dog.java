package dogs;

public abstract class Dog {
    private String name;
    private int age;

    public Dog(String name, int age) {
        this.name = name;
        this.age = age;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public int getAge() {
        return age;
    }

    public void setAge(int age) {
        this.age = age;
    }

    @Override
    public String toString() {
        return "Собака: " + name + ", Лет: " + age;
    }
}

class Type extends Dog {
    private String type;

    public Type(String name, int age, String type) {
        super(name, age);
        this.type = type;
    }

    @Override
    public String toString() {
        System.out.println(super.toString());
        return "Порода: " + type;
    }
}
