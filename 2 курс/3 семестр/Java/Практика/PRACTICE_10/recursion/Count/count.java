package mirea.recursion.Count;

import java.util.Scanner;

public class count {
    public static int c() {
        Scanner in = new Scanner(System.in);
        int n = in.nextInt();
        if (n == 1) {
            int m = in.nextInt();
            if (m == 1) {
                return c() + n + m;
            } else {
                int k = in.nextInt();
                if (k == 1) {
                    return c() + n + m + k;
                } else {
                    return n + m + k;
                }
            }
        }
        else {
            int m = in.nextInt();
            if (m == 1) {
                return c() + n + m;
            } else {
                return n + m;
            }
        }
    }
    public static void main(String[] args)
    {
        System.out.println(c());
    }
}
// 1 0 1 0 0 1