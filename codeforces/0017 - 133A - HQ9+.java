import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String word = sc.nextLine();

        for (int i = 0; i < word.length(); i++) {
            char c = word.charAt(i);
            if (c == 'H' || c == 'Q' || c == '9') {
                System.out.println("YES");
                return;
            }
        }
        System.out.println("NO");
    }
}

