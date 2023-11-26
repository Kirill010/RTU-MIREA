import java.util.Scanner;
import java.util.Stack;

public class Main {
    public static boolean isNum(String symb) {
        try {
            double res = Double.parseDouble(symb);
            return true;
        } catch (Exception e) {
            return false;
        }
    }

    public static boolean isOper(String symb) {
        if (symb.equals("+") || symb.equals("-") || symb.equals("*") || symb.equals("/")) {
            return true;
        }
        return false;
    }

    public static double oper(Double num1, Double num2, String oper) {
        switch (oper) {
            case "+":
                return num1 + num2;
            case "-":
                return num1 - num2;
            case "*":
                return num1 * num2;
            case "/":
                if (num2 == 0) {
                    throw new ArithmeticException("Деление на ноль");
                }
                return num1 / num2;
            default:
                throw new IllegalArgumentException("Неверный оператор");
        }
    }

    public static double calc(String str) {
        String[] expression = str.split(" ");
        Stack<Double> stack = new Stack<>();
        for (String elem : expression) {
            if (isNum(elem)) {
                stack.push(Double.parseDouble(elem));
            } else if (isOper(elem)) {
                if (stack.size() < 2) {
                    throw new IllegalArgumentException("Недостаточное количество чисел");
                } else {
                    double first = stack.pop();
                    double second = stack.pop();
                    stack.push(oper(first, second, elem));
                }
            }
        }
        return stack.pop();
    }

    public static void main(String[] args) {
        Scanner in = new Scanner(System.in);
        String str = in.nextLine();
        System.out.println(calc(str));
    }
}
