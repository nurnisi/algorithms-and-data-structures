import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        evenOdds();
    }

    static void evenOdds() {
        long n = sc.nextLong();
        long k = sc.nextLong();

        long res = 0;
        long one = n % 2 == 0 ? 0 : 1;
        if (k > n / 2 + one) res = (k - (n / 2 + one)) * 2;
        else res = k * 2 - 1;

        System.out.println(res);
    }

}