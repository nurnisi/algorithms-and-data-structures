
import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        magnets();
    }

    static void magnets() {
        int n = Integer.parseInt(sc.nextLine());

        int c = 1, prev = sc.nextInt();
        for (int i = 1; i < n; i++) {
            int curr = sc.nextInt();
            if (curr != prev) c++;
            prev = curr;
        }

        System.out.println(c);
    }
}