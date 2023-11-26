package Items;

public interface Item extends Comparable<Item>{
    String getName();
    String getDescription();
    Integer getPrice();
    String toString();
}
