package MinMax;

public class TestMinMax {
    public static void main(String[] args) {
        MinMax<Double> aDouble = new MinMax<>(new Double[]{68.54, 71.75, 19.21, 7.88});
        printMinMaxInfo(aDouble);
    }

    public static void printMinMaxInfo(MinMax<?> arr) {
        System.out.println(arr);
        System.out.println("Минимальный элемент: " + arr.getMinElement());
        System.out.println("Максимальный элемент: " + arr.getMaxElement());
    }
}