import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String word = sc.nextLine();
        boolean check = true;

        for (int i = 1; i < word.length(); i++) {
            if (word.charAt(i) - 'A' > 26) {
                check = false;
                break;
            }
        }

        if (check) {
            StringBuilder sb = new StringBuilder();

            if (word.charAt(0) - 'A' > 26) {
                String first = word.substring(0, 1).toUpperCase();


                sb.append(first);
                sb.append(word.substring(1).toLowerCase());

                System.out.println(sb.toString());
            } else {
                System.out.println(word.toLowerCase());
            }

        } else {
            System.out.println(word);
        }
    }
}