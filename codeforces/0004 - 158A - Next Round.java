import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int players = sc.nextInt(), k = sc.nextInt() - 1;
        int[] array = new int[players];
        for (int i = 0; i < players; i++) {
            array[i] = sc.nextInt();
        }

        if (array[k] == 0) {
            while (k >= 0 && array[k] == 0) k--;
            k++;
        } else {
            int score = array[k];
            while (k < players && array[k] >= score) k++;
        }

        System.out.println(k);
    }
}