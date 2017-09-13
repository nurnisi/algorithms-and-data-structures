import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        for (int i = 0; i < 5; i++) {
            for (int j = 0; j < 5; j++) {
                if (sc.nextInt() == 1) {
                    System.out.println(Math.abs(i - 2) + Math.abs(j - 2));
                    return;
                }
            }
        }
    }
}

