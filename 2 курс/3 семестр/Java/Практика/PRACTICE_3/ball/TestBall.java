package mirea.lab2_2;

import java.lang.*;

public class TestBall
{
    public static void main(String[] args)
    {
        Ball ball1 = new Ball(10, 10);
        System.out.println(ball1.toString());
        ball1.move(10, 5);
        System.out.println(ball1.toString());
        Ball ball2 = new Ball(5, 3);
        System.out.println(ball2.toString());
    }
}
