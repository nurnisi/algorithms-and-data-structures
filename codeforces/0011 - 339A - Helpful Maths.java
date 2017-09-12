import java.io.*;
import java.util.*;

public class main {
    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        String str = sc.nextLine();
        int ones = 0, twos = 0, threes = 0;
        for (int i = 0; i < str.length(); i += 2) {
            if (str.charAt(i) == '1') ones++;
            else if (str.charAt(i) == '2') twos++;
            else threes++;
        }

        StringBuilder sb = new StringBuilder();
        for (int i = 0; i < ones; i++) {
            sb.append("1+");
        }

        for (int i = 0; i < twos; i++) {
            sb.append("2+");
        }

        for (int i = 0; i < threes; i++) {
            sb.append("3+");
        }

        sb.deleteCharAt(sb.length() - 1);

        System.out.println(sb.toString());
    }
}
