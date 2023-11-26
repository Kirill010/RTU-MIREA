package mirea.mov;

public class Main
{
    public static void main(String[] args)
    {
        MovablePoint movable_point = new MovablePoint(10, 0, 0, 1);
        System.out.println(movable_point);
        movable_point.moveDown();
        movable_point.moveRight();
        System.out.println(movable_point);

        System.out.println();

        MovableCircle movable_circle = new MovableCircle(10, 0, 0, 1, 1);
        System.out.println(movable_circle);
        movable_circle.moveUp();
        movable_circle.moveRight();
        System.out.println(movable_circle);

        System.out.println();

        MovablePoint movable_rectangle = new MovableRectangle(0, 0, 4, 4, 2, 4);
        System.out.println(movable_rectangle);
        movable_rectangle.moveDown();
        movable_rectangle.moveLeft();
        System.out.println(movable_rectangle);
    }
}
