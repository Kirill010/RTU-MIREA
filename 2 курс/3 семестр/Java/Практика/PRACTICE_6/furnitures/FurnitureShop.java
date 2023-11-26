package furnitures;

import java.util.ArrayList;
import java.util.List;

public class FurnitureShop {
    private List<Furniture> furniture_shop_array = new ArrayList<Furniture>();

    public void add_furniture(Furniture furniture) {
        this.furniture_shop_array.add(furniture);
        System.out.println(furniture + ". Эта мебель успешно поступила в магазин");
    }

    public String toString() {
        if (!this.furniture_shop_array.isEmpty()) {
            return "В магазине есть: " + this.furniture_shop_array;
        }
        else {
            return "Магазин пуст!";
        }
    }
}
