package arr;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.Queue;

public class ArrayQueue {
    Queue number = new LinkedList<>();

    public Queue clear(Queue current) {
        current.clear();
        return current;
    }

    public Queue enqueue(int toAdd, ArrayQueue cur) {
        getNumber(cur).add(toAdd);
        return number;
    }

    public Queue add(ArrayQueue cur, int toAdd) {
        cur.getNumber(cur).add(toAdd);
        return cur.getNumber(cur);
    }

    public Queue getNumber(ArrayQueue cur) {
        return cur.number;
    }

    public int dequeue(ArrayQueue cur) {
        int toRes = (int) cur.getNumber(cur).element();
        cur.getNumber(cur).poll();
        return toRes;
    }

    public int size(ArrayQueue cur) {
        return cur.getNumber(cur).size();
    }

    public boolean isEmpty(ArrayQueue cur) {
        return cur.getNumber(cur).isEmpty();
    }

    public static void main(String[] args) {
        ArrayQueue adt = new ArrayQueue();
        adt.add(adt, 23);
        adt.add(adt, 24);
        adt.add(adt, 25);
        System.out.println("Queue: " + adt.getNumber(adt));
        int removedNumber = adt.dequeue(adt);
        System.out.println("Removed Element: " + removedNumber);
        System.out.println("Queue after deletion: " + adt.getNumber(adt));
    }
}