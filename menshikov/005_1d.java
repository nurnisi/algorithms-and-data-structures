import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        d1();
    }

    static void d1() {
        int x1 = sc.nextInt(), y1 = sc.nextInt();
        int x2 = sc.nextInt(), y2 = sc.nextInt();
        int x3 = sc.nextInt(), y3 = sc.nextInt();
        int x0 = sc.nextInt(), y0 = sc.nextInt();

        if (isIn2(x1, y1, x2, y2, x3, y3, x0, y0)) System.out.println("In");
        else System.out.println("Out");
    }

    static boolean isIn(int x1, int y1, int x2, int y2, int x3, int y3, int x0, int y0) {
        long a = x3 * (y1 - y2) + y3 * (x2 - x1) + (x1 * y2 - y1 * x2);
        long b = x0 * (y1 - y2) + y0 * (x2 - x1) + (x1 * y2 - y1 * x2);

        return a * b >= 0;
    }