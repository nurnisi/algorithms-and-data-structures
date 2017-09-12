import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String word = sc.nextLine();
        StringBuilder sb = new StringBuilder();
        String first = word.substring(0, 1).toUpperCase();


        sb.append(first);
        sb.append(word.substring(1));

        System.out.println(sb.toString());
    }
}

