import java.util.*;
import java.io.*;

public class Main {
    private static Scanner sc;

    public static void main(String[] args) throws NullPointerException {
        sc = new Scanner(System.in);

        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        long output1 = a / c;
        if (a % c > 0) output1++;

        long output2 = b / c;
        if (b % c > 0) output2++;

        System.out.println(output1 * output2);
    }
}