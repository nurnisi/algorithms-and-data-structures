import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        designTutorial();
    }

    static boolean isComposite(int n) {
        for (int i = 2; i * i <= n; i++)
            if (n % i == 0)
                return true;
        return false;
    }

    static void designTutorial() {
        int n = sc.nextInt();
        for (int i = 2; i * 2 <= n; i++) {
            if (isComposite(i) && isComposite(n - i)) {
                System.out.println(i + " " + (n - i));
                return;
            }
        }
    }

}

//easy implementation
static void designTutorial() {
    int n = sc.nextInt();

    if (n % 2 == 0) System.out.println((n - 8) + " " + 8);
    else System.out.println((n - 9) + " " + 9);
}