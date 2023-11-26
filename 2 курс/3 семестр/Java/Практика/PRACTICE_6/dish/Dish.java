package dish;

public abstract class Dish {
    private String name;
    private String type;

    public Dish(String name, String type) {
        this.name = name;
        this.type = type;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getType() {
        return type;
    }

    public void setType(String type) {
        this.type = type;
    }

    public abstract void name();
}

class Plate extends Dish {
    private String color;

    public Plate(String name, String type, String color) {
        super(name, type);
        this.color = color;
    }

    public void name() {
        System.out.println("Посуда: " + super.getName() + ", Материал: " + super.getType() + ", Цвет: " + color);
    }
}

class Tableware extends Dish {
    private String inst;

    public Tableware(String name, String type, String inst) {
        super(name, type);
        this.inst = inst;
    }

    public void name() {
        //System.out.println("Посуда: " + super.getName() + ", Материал: " + super.getType() + ", Прибор: " + inst);
        System.out.println("Посуда: " + inst + ", Материал: " + super.getType());
    }
}