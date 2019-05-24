import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        function();
    }

    static void function() {
        long n = sc.nextLong();

        if (n % 2 == 0) System.out.println(n / 2);
        else System.out.println(n / 2 - n);
    }

}