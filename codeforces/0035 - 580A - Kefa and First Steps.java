import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        firstSteps();
    }

    static void firstSteps() {
        int n = Integer.parseInt(sc.nextLine());

        int counter = 1, max = 1, prev = sc.nextInt();

        for (int i = 1; i < n; i++) {
            int curr = sc.nextInt();
            if (prev <= curr) counter++;
            else counter = 1;

            prev = curr;
            max = Math.max(max, counter);
        }

        System.out.println(max);
    }

}