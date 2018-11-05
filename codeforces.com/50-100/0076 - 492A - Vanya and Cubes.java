import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        pyramids();
    }

    static void pyramids() {
        int n = sc.nextInt();

        int next = 1;
        int level = 0;

        while (n >= next) {
            level++;
            n -= next;
            next = (level + 1) * (level + 2) / 2;
        }
        System.out.println(level);
    }
}