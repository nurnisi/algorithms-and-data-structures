import java.util.*;
import java.io.*;

public class main {
    static Scanner sc = new Scanner(System.in);
    public static void main(String[] args) {
        int i = sc.nextInt();
        for (; i >= 0; i--) {
            String word = sc.nextLine();
            int length = word.length();
            if (length > 10) word = String.format("%s%s%s", word.charAt(0), length - 2, word.charAt(length - 1));
            System.out.println(word);
        }
    }
}