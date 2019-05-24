import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        hulk();
    }

    static void hulk() {
        int n = sc.nextInt();

        StringBuilder sb = new StringBuilder();
        sb.append("I hate ");
        for (int i = 0; i < n - 1; i++) {
            if (i % 2 == 0) sb.append("that I love ");
            else sb.append("that I hate ");
        }
        sb.append("it");

        System.out.println(sb.toString());
    }
}