import java.lang.reflect.Array;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a2_3();
    }

    static void a2_3() {
        List<Integer> primes = getPrimes(1009);

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

    static List<Integer> getPrimes(int m) {
        int[] arr = new int[m + 1];
        arr[0] = 1;
        arr[1] = 1;

        int i = 2;
        while (i < arr.length) {
            if (arr[i] == 0) {
                int j = i * 2;
                while (j < arr.length) {
                    arr[j] = 1;
                    j += i;
                }
            }
            i++;
        }

        List<Integer> primes = new ArrayList<>();
        for (int j = 0; j < arr.length; j++)
            if (arr[j] == 0)
                primes.add(j);

        return primes;
    }

    static void a2_2() {
        List<Integer> primes = new ArrayList<>();
        for (int i = 2; i <= 1009; i++)
            if (isPrime(i))
                primes.add(i);

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