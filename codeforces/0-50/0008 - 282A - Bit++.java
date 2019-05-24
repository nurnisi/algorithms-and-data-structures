import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int i = Integer.parseInt(sc.nextLine());

        int x = 0;
        for (int j = 0; j < i; j++) {
            String operation = sc.nextLine();
            if (operation.charAt(1) == '-') --x;
            else ++x;
        }

        System.out.println(x);
    }
}
