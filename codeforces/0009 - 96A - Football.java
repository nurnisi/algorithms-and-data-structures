import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String str = sc.nextLine();
        int counter = 1;
        for (int i = 1; i < str.length(); i++) {
            if (str.charAt(i - 1) == str.charAt(i)) counter++;
            else counter = 1;

            if (counter == 7) {
                System.out.println("YES");
                return;
            }
        }

        System.out.println("NO");
    }
}
