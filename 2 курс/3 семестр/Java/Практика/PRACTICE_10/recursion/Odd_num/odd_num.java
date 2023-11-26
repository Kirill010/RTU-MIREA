package mirea.recursion.Odd_num;
// нечетные номера
public class odd_num {
    public static void rec() {
        java.util.Scanner in = new java.util.Scanner(System.in);
        int n = in.nextInt();
        if (n > 0) {
            int m = in.nextInt();
            System.out.println(n);
            if (m > 0) {
                rec();
            }
        }
    }
    public static void main(String[] args) {
        rec();
    }
}
// 7 2 9 5 0