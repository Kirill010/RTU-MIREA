package Orders;

import Customer.Customer;
import Items.Item;

import java.util.Arrays;
import java.util.HashSet;

public class TableOrder implements Order {
    int size = 0;
    Item[] items;
    Customer customer;

    public TableOrder(Customer customer) {
        this.items = new Item[0];
        this.customer = customer;

    }

    public TableOrder() {
        this.items = new Item[0];
    }

    @Override
    public boolean add(Item item) {
        if (item == null) return false;
        Item[] newItemsList = new Item[size + 1];
        System.arraycopy(items, 0, newItemsList, 0, items.length);
        newItemsList[items.length] = item;
        items = newItemsList;
        size++;
        return true;
    }

    @Override
    public String[] itemsName() {
        HashSet<String> hashNames = new HashSet<>(size);
        for (int i = 0; i < size; i++) {
            hashNames.add(items[i].getName());
        }
        String[] names = new String[hashNames.size()];
        return hashNames.toArray(names);
    }

    @Override
    public int itemsQuantity() {
        return size;
    }

    @Override
    public int itemsQuantity(String itemName) {
        int count = 0;
        for (int i = 0; i < size; i++) {
            if (items[i].getName().equals(itemName)) count++;
        }
        return count;
    }

    @Override
    public int itemsQuantity(Item item) {
        return itemsQuantity(item.getName());
    }

    @Override
    public Item[] getItems() {
        return items;
    }

    @Override
    public boolean remove(String itemName) {
        int index = -1;
        for (int i = 0; i < items.length; i++) {
            if (items[i].getName().equals(itemName)) {
                index = i;
            }
        }

        if (index == -1) return false;
        Item[] temp = items;
        items = new Item[temp.length - 1];
        System.arraycopy(temp, 0, items, 0, index);
        System.arraycopy(temp, index + 1, items, index, temp.length - index - 1);
        size--;
        return false;
    }

    @Override
    public boolean remove(Item item) {
        return remove(item.getName());
    }

    @Override
    public int removeAll(String itemName) {
        int count = 0;
        while (contains(itemName)) {
            remove(itemName);
        }
        return count;
    }

    @Override
    public int removeAll(Item item) {
        return removeAll(item.getName());
    }

    public boolean contains(String itemName) {
        for (int i = 0; i < size; i++) {
            if (items[i].getName().equals(itemName)) return true;
        }
        return false;
    }

    @Override
    public Item[] sortedItemsByCostDesc() {
        Arrays.sort(items);
        return items;
    }

    @Override
    public int costTotal() {
        int cost = 0;
        for (int i = 0; i < size; i++) {
            cost += items[i].getPrice();
        }
        return cost;
    }

    public int getSize(){
        return size;
    }

    @Override
    public Customer getCustomer() {
        return this.customer;
    }

    @Override
    public void setCustomer(Customer customer) {
        this.customer = customer;
    }
}
