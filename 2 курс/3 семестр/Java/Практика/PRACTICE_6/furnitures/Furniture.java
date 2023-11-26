package furnitures;

public abstract class Furniture {
    protected String name;
    private String material;
    public Furniture(String name, String material){
        this.name = name;
        this.material = material;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getMaterial() {
        return material;
    }

    public void setMaterial(String material) {
        this.material = material;
    }

    public abstract String cost();

    @Override
    public String toString() {
        return "Мебель: " + name + ", Материал: " + material;
    }
}

class Type extends Furniture {
    private String type;

    public Type(String name, String material, String type) {
        super(name, material);
        this.type = type;
    }

    @Override
    public String cost() {
        return "Стоит на " + type;
    }
    @Override
    public String toString() {
        System.out.println(super.toString());
        return name;
    }
}