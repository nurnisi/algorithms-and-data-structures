import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        presents();
    }

    static void presents() {
        int n = Integer.parseInt(sc.next());
        int[] array = new int[n];

        for (int i = 0; i < n; i++) {
            array[i] = sc.nextInt();
        }

        int[] res = new int[n];
        for (int i = 0; i < n; i++) {
            res[array[i] - 1] = i + 1;
        }

        for (int i : res) System.out.print(i + " ");
    }

}