package arr;

import java.util.Queue;
import java.util.LinkedList;

public class ArrayQueueADT {
    Queue number = new LinkedList<>();

    public Queue clear(Queue current) {
        current.clear();
        return current;
    }

    public ArrayQueueADT() {
        this.number.add(13);
        this.number.add(64);
        this.number.add(67);
    }

    public Queue enqueue(int toAdd) {
        this.number.add(toAdd);
        return number;
    }

    public Queue getNumber() {
        return this.number;
    }

    public int dequeue() {
        int toRes = (int) this.number.element();
        this.number.poll();
        return toRes;
    }

    public int size() {
        return this.number.size();
    }

    public boolean isEmpty() {
        return this.number.isEmpty();
    }

    public void out() {
        System.out.println(this.number);
    }

    public static void main(String[] args) {
        ArrayQueueADT adt = new ArrayQueueADT();
        System.out.print("Queue is ");
        adt.out();
        int removedNumber = adt.dequeue();
        System.out.println("Removed Element: " + removedNumber);
        System.out.print("Queue after deletion: ");
        adt.out();
    }
}