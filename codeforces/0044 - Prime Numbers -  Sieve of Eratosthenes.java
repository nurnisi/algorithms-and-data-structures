import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        sieve(1000);
    }

    static void sieve(int n) {
        if (n < 2) return;

        int[] isComposite = new int[n + 1];

        isComposite[0] = 1;
        isComposite[1] = 1;

        for (int i = 2; i * i <= n; i++) {
            if (isComposite[i] != 1) {
                for (int j = i * i; j <= n; j += i) {
                    isComposite[j] = 1;
                }
            }
        }

        for (int i = 0; i < isComposite.length; i++) {
            if (isComposite[i] != 1) System.out.println(i);
        }
    }

}