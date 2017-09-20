import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        insomnia();
    }

    static void insomnia() {
        int k = sc.nextInt(),
            l = sc.nextInt(),
            m = sc.nextInt(),
            n = sc.nextInt(),
            d = sc.nextInt();

        int counter = 0;
        for (int i = 0; i < d; i++) {
            if ((i + 1) % k == 0 || (i + 1) % l == 0
                || (i + 1) % m == 0 || (i + 1) % n == 0) {
                counter++;
            }
        }

        System.out.println(counter);
    }
}