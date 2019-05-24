import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        dubstep();
    }

    static void dubstep() {
        String dubstep = sc.next();
        StringBuilder sb = new StringBuilder();

        for (int i = 0; i < dubstep.length(); i++) {
            if (i + 2 < dubstep.length() &&
                    dubstep.charAt(i) == 'W' &&
                    dubstep.charAt(i + 1) == 'U' &&
                    dubstep.charAt(i + 2) == 'B') {
                if (sb.length() != 0) System.out.print(sb.toString() + " ");
                sb.delete(0, sb.length());
                i += 2;
            } else sb.append(dubstep.charAt(i));
        }
        if (sb.length() != 0) System.out.print(sb.toString() + " ");
    }

}