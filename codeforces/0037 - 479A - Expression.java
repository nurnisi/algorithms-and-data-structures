import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        expression();
    }

    static void expression() {
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        int d = a + b + c;
        int e = a * (b + c);
        int f = a * b * c;
        int g = (a + b) * c;

        System.out.println(Math.max(d, Math.max(e, Math.max(f, g))));
    }

}