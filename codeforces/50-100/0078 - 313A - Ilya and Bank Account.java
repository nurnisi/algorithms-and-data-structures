import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        bankAccount();
    }

    static void bankAccount() {
        long n = sc.nextLong();

        if (n >= 0) {
            System.out.println(n);
            return;
        }

        long n1 = n / 10;
        long n2 = n / 100 * 10 + n % 10;
        System.out.println(n1 > n2 ? n1 : n2);
    }

}