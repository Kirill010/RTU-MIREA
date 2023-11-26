package Price;

public class Home implements Priceable {
    private int price;

    Home(int price) {
        this.price = price;
    }

    public int getPrice() {
        return price;
    }

}
