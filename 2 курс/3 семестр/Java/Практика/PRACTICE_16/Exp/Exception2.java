package Exp;

import java.util.Scanner;

public class Exception2 {
    public void exceptionDemo() {
        Scanner myScanner = new Scanner(System.in);
        System.out.print("Enter an integer ");
        String intString = myScanner.next();
        int i = Integer.parseInt(intString);
        System.out.println(2 / i);
    }

    public void exceptionDemo1() {
        Scanner myScanner = new Scanner(System.in);
        System.out.print("Enter an integer ");
        String intString = myScanner.next();
        int i = 2;
        try {
            i = Integer.parseInt(intString);
            System.out.println(2 / i);
        } catch (ArithmeticException e) {
            System.out.println("Attempted division by zero");
        } catch (NumberFormatException e) {
            System.out.println("The program is waiting for the input of an integer value");
        }
    }

    public static void main(String[] args) {
        Exception2 q = new Exception2();
        //q.exceptionDemo();
        q.exceptionDemo1();
    }
}

/*
    Exception in thread "main" java.lang.NumberFormatException: For input string: "Qwerty"
        at java.base/java.lang.NumberFormatException.forInputString(NumberFormatException.java:67)
        at java.base/java.lang.Integer.parseInt(Integer.java:665)
        at java.base/java.lang.Integer.parseInt(Integer.java:781)
        at Exp.Exception2.exceptionDemo(Exception2.java:10)
        at Exp.Exception2.main(Exception2.java:16)
*/
