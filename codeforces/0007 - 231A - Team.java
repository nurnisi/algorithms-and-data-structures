import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int problems = sc.nextInt();
        int solutions = 0;

        for (int i = 0; i < problems; i++) {
            int a = sc.nextInt();
            int b = sc.nextInt();
            int c = sc.nextInt();

            if (a + b + c > 1) solutions++;
        }

        System.out.println(solutions);
    }
}
