import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        chess();
    }

    static void chess() {
        int n = Integer.parseInt(sc.nextLine());
        String s = sc.nextLine();

        int danik = 0;
        for (int i = 0; i < n; i++) {
            if (s.charAt(i) == 'D') danik++;
        }

        if (danik > n - danik) System.out.println("Danik");
        else if (danik < n - danik) System.out.println("Anton");
        else System.out.println("Friendship");
    }
}