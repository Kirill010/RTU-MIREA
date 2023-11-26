package Orders;

import Exceptions.IllegalTableNumber;
import Exceptions.OrderAlreadyAddedException;
import Items.Item;

public class TableOrdersManager implements OrderManager {
    Order[] orders;

    public TableOrdersManager() {
        this.orders = new Order[16];
    }

    @Override
    public int itemsQuantity(String itemName) {
        int count = 0;
        for (int i = 0; i < orders.length; i++) {
            count += orders[i].itemsQuantity(itemName);
        }
        return count;
    }

    @Override
    public int itemsQuantity(Item item) {
        return itemsQuantity(item.getName());
    }

    @Override
    public Order[] getOrders() {
        return orders;
    }

    @Override
    public int ordersCostSummary() {
        int sum = 0;
        for (int i = 0; i < orders.length; i++) {
            sum += orders[i].costTotal();
        }
        return sum;
    }

    public void add(Order order, int tableNumber) throws IllegalTableNumber, OrderAlreadyAddedException {
        if (tableNumber < 1 || tableNumber > 15) throw new IllegalTableNumber("Bad table number");
        if (orders[tableNumber] == null) {
            orders[tableNumber] = order;
        } else {
            throw new OrderAlreadyAddedException("Order already exist");
        }
    }

    public void addItem(Item item, int tableNumber) throws OrderAlreadyAddedException {
        if (orders[tableNumber] == null) {
            orders[tableNumber] = new TableOrder();
            orders[tableNumber].add(item);
        } else {
            throw new OrderAlreadyAddedException("Order already existed");
        }
    }

    public int freeTableNumber() {
        for (int i = 1; i < 16; i++) {
            if (orders[i] == null) return i;
        }
        return -1;
    }

    public int[] freeTableNumbers() {
        int count = 0;
        for (int i = 1; i < 16; i++) {
            if (orders[i] == null) count++;
        }

        int[] freeTables = new int[count];
        int j = 1;
        for (int i = 1; i < 16; i++) {
            if (orders[i] == null) freeTables[j] = i;
            j++;
        }
        return freeTables;
    }

    public Order getOrder(int tableNumber) throws IllegalTableNumber {
        if (tableNumber < 1 || tableNumber > 15) throw new IllegalTableNumber("Bad table number");
        return orders[tableNumber];
    }

    public void remove(int tableNumber) throws IllegalTableNumber {
        if (tableNumber < 1 || tableNumber > 15) throw new IllegalTableNumber("Bad table number");
        orders[tableNumber] = null;
    }

    int remove(Order order) {
        for (int i = 1; i < orders.length; i++) {
            if (orders[i].equals(order)) {
                remove(orders[i]);
                return i;
            }
        }
        return -1;
    }

    public int removeAll(Order order) {
        int count = 0;
        for (int i = 1; i < orders.length; i++) {
            if (orders[i].equals(order)) {
                remove(orders[i]);
                count++;
            }
        }
        return count;
    }
}
