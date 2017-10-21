import java.io.*;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        joke();
    }

    static void joke() {
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        String s3 = sc.nextLine();

        if (s1.length() + s2.length() != s3.length()) {
            System.out.println("NO");
            return;
        }

        String s4 = s1 + s2;
        char[] arr1 = s4.toCharArray();
        char[] arr2 = s3.toCharArray();

        Arrays.sort(arr1);
        Arrays.sort(arr2);

        for (int i = 0; i < arr1.length; i++) {
            if (arr1[i] != arr2[i]) {
                System.out.println("NO");
                return;
            }
        }

        System.out.println("YES");
    }
}