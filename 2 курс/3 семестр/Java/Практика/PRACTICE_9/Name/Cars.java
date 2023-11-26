package Name;

public class Cars implements Nameable{
    private String model;
    Cars(String model){
        this.model = model;
    }

    public String getName() {
        return model;
    }
}