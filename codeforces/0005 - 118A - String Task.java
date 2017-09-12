import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String input = sc.nextLine().toLowerCase();
        StringBuilder output = new StringBuilder();

        Set<Character> set = new HashSet<>();
        set.add('a');
        set.add('o');
        set.add('y');
        set.add('e');
        set.add('u');
        set.add('i');

        for (char c : input.toCharArray()) {
            if (!set.contains(c)) {
                output.append("." + c);
            }
        }

        System.out.println(output.toString());
    }
}
