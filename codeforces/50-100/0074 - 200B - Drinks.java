import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        lanterns();
    }

    static void lanterns() {
        int n = sc.nextInt();
        
        double sum = 0;
        for (int i = 0; i < n; i++) {
            sum += sc.nextDouble();
        }

        System.out.println(sum / n);
    }
}