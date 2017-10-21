import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        snake();
    }

    static void snake() {
        int n = sc.nextInt();
        int m = sc.nextInt();

        StringBuilder sb1 = new StringBuilder();
        StringBuilder sb2 = new StringBuilder();
        StringBuilder sb3 = new StringBuilder();
        sb3.append('#');
        for (int i = 1; i < m; i++) {
            sb1.append('#');
            sb2.append('.');
            sb3.append('.');
        }
        sb1.append('#');
        sb2.append('#');

        String s1 = sb1.toString(), s2 = sb2.toString(), s3 = sb3.toString();
        
        for (int i = 1; i <= n; i++) {
            if (i % 2 == 1) System.out.println(s1);
            else if ((i / 2) % 2 == 1) System.out.println(s2);
            else System.out.println(s3);
        }
    }
}