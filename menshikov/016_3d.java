import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        d3();
    }

    static void d3() {
        int a = sc.nextInt(),
                b = sc.nextInt(),
                c = sc.nextInt(),
                d = sc.nextInt();

        int max1 = a > b ? a : b,
                min1 = a < b ? a : b,
                max2 = c > d ? c : d,
                min2 = c < d ? c : d;

        if (max1 <= max2 && min1 <= min2) System.out.println("Possible");
        else {
            double diag = Math.sqrt(Math.pow(max2, 2) + Math.pow(min2, 2));
            if (diag - min1 >= max1) System.out.println("Possible");
            else System.out.println("Impossible");
        }
    }
}