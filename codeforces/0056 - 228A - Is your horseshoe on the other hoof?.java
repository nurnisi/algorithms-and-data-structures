import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        horseshoes();
    }

    static void horseshoes() {
        Set<Integer> set = new HashSet<>();
        for (int i = 0; i < 4; i++) {
            int cur = sc.nextInt();
            if (!set.contains(cur)) set.add(cur);
        }

        System.out.println(4 - set.size());
    }
}