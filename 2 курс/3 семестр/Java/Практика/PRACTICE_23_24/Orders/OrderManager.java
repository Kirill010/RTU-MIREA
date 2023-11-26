package Orders;

import Items.Item;

import java.util.HashMap;
import java.util.Map;

public interface OrderManager {
    Map<String, Order> ordersHashMap = new HashMap<>();
    int itemsQuantity(String itemName);
    int itemsQuantity(Item item);
    Order[] getOrders();
    int ordersCostSummary();
}
