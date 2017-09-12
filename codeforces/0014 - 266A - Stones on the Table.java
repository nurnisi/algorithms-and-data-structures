import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        int i = Integer.parseInt(sc.nextLine());
        String str = sc.nextLine();
        int counter = 0;

        for (int j = 1; j < str.length(); j++) {
            if (str.charAt(j - 1) == str.charAt(j)) counter++;
        }

        System.out.println(counter);
    }
}

