import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        game();
    }

    static void game() {
        int levels = sc.nextInt();

        int x = sc.nextInt();
        int[] xArr = new int[x];
        for (int i = 0; i < x; i++) {
            xArr[i] = sc.nextInt();
        }

        int y = sc.nextInt();
        int[] yArr = new int[y];
        for (int i = 0; i < y; i++) {
            yArr[i] = sc.nextInt();
        }

        Arrays.sort(xArr);
        Arrays.sort(yArr);

        int curr = 1, i = 0, j = 0;
        while (i < x && j < y) {
            if (xArr[i] == curr && yArr[j] == curr) {
                i++;
                j++;
            } else if (xArr[i] == curr) i++;
            else if (yArr[j] == curr) j++;
            else {
                System.out.println("Oh, my keyboard!");
                return;
            }

            if (curr == levels) {
                System.out.println("I become the guy.");
                return;
            }

            curr++;
        }

        while (i < x) {
            if (xArr[i] == curr) {
                if (curr == levels) {
                    System.out.println("I become the guy.");
                    return;
                } else {
                    curr++;
                    i++;
                }
            } else {
                System.out.println("Oh, my keyboard!");
                return;
            }
        }

        while (j < y) {
            if (yArr[j] == curr) {
                if (curr == levels) {
                    System.out.println("I become the guy.");
                    return;
                } else {
                    curr++;
                    j++;
                }
            } else {
                System.out.println("Oh, my keyboard!");
                return;
            }
        }

        System.out.println("Oh, my keyboard!");
    }

}