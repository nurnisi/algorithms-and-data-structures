import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        contests();
    }

    static void contests() {
        int n = sc.nextInt();

        int max = sc.nextInt();
        int min = max;
        int counter = 0;

        for (int i = 1; i < n; i++) {
            int next = sc.nextInt();
            if (max < next) {
                counter++;
                max =  next;
            }
            if (min > next) {
                counter++;
                min = next;
            }
        }

        System.out.println(counter);
    }
}