package Price;

public class Guitar implements Priceable {
    private int price;

    Guitar(int price) {
        this.price = price;
    }

    public int getPrice() {
        return price;
    }
}
