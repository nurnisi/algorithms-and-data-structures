import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a1();
    }

    static void a1() {
        int n = sc.nextInt(), m = sc.nextInt();
        boolean check = true;
        while (n <= m) {
            if (isPrime(n)) {
                check = false;
                System.out.println(n);
            }
            n++;
        }
        if (check) System.out.println("Absent");
    }

    static boolean isPrime(int n) {
        int m = 2;
        while (m * m <= n) {
            if (n % m == 0) return false;
            m++;
        }
        return true;
    }
}