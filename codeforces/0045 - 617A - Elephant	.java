import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        elephant();
    }

    static void elephant() {
        int n = sc.nextInt();
        System.out.println(n / 5 + (n % 5 != 0 ? 1 : 0));
    }

}