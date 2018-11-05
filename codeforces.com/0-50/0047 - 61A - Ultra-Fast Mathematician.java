import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        ultraMath();
    }

    static void ultraMath() {
        String line1 = sc.nextLine(), line2 = sc.nextLine();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < line1.length(); i++) {
            if (line1.charAt(i) == line2.charAt(i)) sb.append(0);
            else sb.append(1);
        }

        System.out.println(sb.toString());
    }
}