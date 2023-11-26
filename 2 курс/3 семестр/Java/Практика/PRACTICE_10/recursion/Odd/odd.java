package mirea.recursion.Odd;
// нечетные числа
public class odd {
    public static void o() {
        java.util.Scanner in = new java.util.Scanner(System.in);
        int n = in.nextInt();
        if (n > 0) {
            if (n % 2 == 1) {
                System.out.println(n);
                o();
            } else {
                o();
            }
        }
    }
    public static void main(String[] args) {
        o();
    }
}
// 3 1 2 0