import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a2_2();
    }

    static void a2_2() {
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= 1000; i++)
            if (isPrime(i)) primes.add(i);

        int n = sc.nextInt(), m = sc.nextInt();

        int sqrt = (int) Math.sqrt(n);
        boolean globCheck = true;

        while (n <= m) {
            int i = 0;
            boolean check = true;
            while (primes.get(i) <= sqrt) {
                if (n % primes.get(i) == 0) {
                    check = false;
                    break;
                }
                i++;
            }
            if (check) {
                globCheck = false;
                System.out.println(n);
            }
            n++;
            if ((int) Math.pow(sqrt + 1, 2) == n) sqrt++;
        }
        if (globCheck) System.out.println("Absent");
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