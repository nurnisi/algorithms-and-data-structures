import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int cost = sc.nextInt();
        int dollars = sc.nextInt();
        int bananas = sc.nextInt();

        int total = cost * ((bananas * (bananas + 1)) / 2) - dollars;
        System.out.println(total > 0 ? total : 0);
    }
}