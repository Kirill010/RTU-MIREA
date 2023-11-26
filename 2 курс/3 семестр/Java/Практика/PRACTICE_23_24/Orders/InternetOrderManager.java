package Orders;

import Items.Item;

public class InternetOrderManager implements OrderManager {
    public int all_cost = 0;
    QueueNode head;
    QueueNode tail;
    int size;

    public void add(Order order) {
        if (order == null) {
            return;
        }
        all_cost += order.costTotal();
        if (size == 0) {
            head = new QueueNode(null, order, null);
            tail = head;
        } else {
            QueueNode secondLast = tail;
            tail = new QueueNode(secondLast, order, null);
            secondLast.next = tail;
        }
        size++;
    }

    Order remove() {
        Order removable = head.value;
        head = head.next;
        head.prev = null;
        return removable;
    }

    @Override
    public int itemsQuantity(String itemName) {
        int count = 0;
        QueueNode tmp = head;
        for (int i = 0; i < size; i++) {
            String[] itemsName = tmp.value.itemsName();
            for (String names : itemsName) {
                if (names.equals(itemName)) {
                    count++;
                }
            }
            tmp = tmp.next;
        }
        return count;
    }

    @Override
    public int itemsQuantity(Item item) {
        int count = 0;
        QueueNode tmp = head;
        for (int i = 0; i < size; i++) {
            String[] itemsName = tmp.value.itemsName();
            for (String names : itemsName) {
                if (names.equals(item.getName())) {
                    count++;
                }
            }
            tmp = tmp.next;
        }
        return count;
    }

    @Override
    public Order[] getOrders() {
        Order[] allOrders = new Order[size];
        QueueNode tmp = head;
        for (int i = 0; i < size; i++) {
            allOrders[i] = tmp.value;
            tmp = tmp.next;
        }
        return allOrders;
    }

    @Override
    public int ordersCostSummary() {
        return all_cost;
    }

    public int getSize() {
        return size;
    }

    private static class QueueNode {
        QueueNode next;
        QueueNode prev;
        Order value;

        public QueueNode(QueueNode prev, Order value, QueueNode next) {
            this.next = next;
            this.prev = prev;
            this.value = value;
        }
    }
}
