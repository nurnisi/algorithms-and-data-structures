import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int i = sc.nextInt();

        int passengers = 0;
        int max = 0;

        for (int j = 0; j < i; j++) {
            int a = sc.nextInt();
            int b = sc.nextInt();

            passengers -= a;
            passengers += b;

            if (passengers > max) max = passengers;
        }

        System.out.println(max);
    }
}