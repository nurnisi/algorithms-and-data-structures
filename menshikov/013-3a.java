import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a3();
    }

    static void a3_2_optimized() {
        int n = sc.nextInt();

        int i = 2;
        while (i * i <= n) {
            if (n % i == 0) {
                n /= i;
                System.out.print(i + (n != 1 ? "*" : ""));
            } else if (i == 2) i++;
            else i += 2;
        }

        if (n != 1) System.out.print(n);
    }

    static void a3() {
        int n = sc.nextInt();

        int i = 2;
        while (i * i <= n) {
            if (n % i == 0) {
                n /= i;
                System.out.print(i + (n != 1 ? "*" : ""));
            } else i++;
        }

        if (n != 1) System.out.print(n);
    }
}