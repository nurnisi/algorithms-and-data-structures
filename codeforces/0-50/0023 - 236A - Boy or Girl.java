import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String str = sc.nextLine();
        Set<Character> set = new HashSet<>();

        for (char c : str.toCharArray()) {
            if (!set.contains(c)) set.add(c);
        }

        if (set.size() % 2 == 1) System.out.println("IGNORE HIM!");
        else System.out.println("CHAT WITH HER!");
    }
}