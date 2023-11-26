package wait;

public class UnfairWaitList<E> extends WaitList<E> {

    public UnfairWaitList() {
        super();
    }

    public void remove(E element) {
        boolean removed = false;
        for (int i = 0; i < components.size(); i++) {
            E el = components.remove();
            if (!removed && el.equals(element)) {
                removed = true;
            } else {
                components.add(el);
            }
        }
        if (removed) {
            components.add(components.remove());
        }
    }


    public void moveToBack(E element) {
        int prevSize = components.size();
        remove(element);
        if (components.size() < prevSize) {
            components.add(element);
        }

    }
}
