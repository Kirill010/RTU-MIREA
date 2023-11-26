package ball;
import java.lang.*;
public class Ball {
    private String name;
    private String material;

    public Ball(String n, String m) {
        name = n;
        material = m;
    }

    public Ball(String n) {
        name = n;
    }

    public Ball() {
        name = "Untitled";
        material = "Untitled";
    }

    public void setName(String name) {
        this.name = name;
    }
    public void setmaterial(String material) {
        this.material = material;
    }

    public String getName(String name) {
        return name;
    }
    public String getmaterial(String material) {
        return material;
    }

    @Override
    public String toString() {
        return this.name + " мяч, Материал: "+ this.material;
    }
}
