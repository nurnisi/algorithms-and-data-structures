import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a2();
    }

    static void a2() {
        int n = sc.nextInt(), m = sc.nextInt();
        boolean check = false;
        while (n < m + 1) {
            if (isPrime(n)) {
                System.out.println(n);
                check = true;
            }
            n++;
        }
        if (!check) System.out.println("Absent");
    }

    static boolean isPrime(int i) {
        int n = 2;
        while (n * n <= i) {
            if (i % n == 0) return false;
            n++;
        }
        return true;
    }
}