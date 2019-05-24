import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        sticks();
    }

    static void sticks() {
        int n = sc.nextInt();
        int m = sc.nextInt();

        if (Math.min(n, m) % 2 == 0) System.out.println("Malvika");
        else System.out.println("Akshat");
    }

}