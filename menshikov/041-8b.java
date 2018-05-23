import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        b8();
    }

    //my solution: time limit exceeded
    static int[] lettersInDigits = new int[]{0,0,3,3,3,3,3,4,3,4};
    static int[][] letters, digitsPressed;
    static int len = 1, N, ans = 0;

    static void b8() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        //read input
        N = sc.nextInt();
        String sms = sc.next();

        //get digit location and index of each letter
        letters = getLetters();

        //init array to count how many times each digit was pressed
        int smsLen = sms.length();
        digitsPressed = new int[smsLen][2];
        //add first digit to array as initial parameter
        digitsPressed[0][0] = letters[sms.charAt(0) - 'A'][0];
        digitsPressed[0][1] = letters[sms.charAt(0) - 'A'][1];
        int total = letters[sms.charAt(0) - 'A'][1];
        //count how many times each digit was pressed
        int cur = 1;
        while (cur < smsLen) {
            int ch = sms.charAt(cur) - 'A', prev = sms.charAt(cur - 1) - 'A';
            if (letters[ch][0] == letters[prev][0]) {
                digitsPressed[len - 1][1] += letters[ch][1];
            } else {
                digitsPressed[len][0] = letters[ch][0];
                digitsPressed[len][1] = letters[ch][1];
                len++;
            }
            total += letters[ch][1];
            cur++;
        }

        //check if total number of digits pressed is less than initial word
        if (total < N) {
            pw.println(0);
        } else {
            helper(0,0,0);
            pw.println(ans);
        }
        pw.close();
    }

    //recursive method to check all possible variants
    static void helper(int cur, int total, int count) {
        if (count > N) return;
        else if (cur == len) {
            if (count == N) ans++;
        } else {
            int ch = digitsPressed[cur][0], dp = digitsPressed[cur][1];
            for (int i = 1; i <= lettersInDigits[ch]; i++) {
                if (total + i == dp) {
                    helper(cur + 1, 0, count + 1);
                    break;
                } else {
                    helper(cur, total + i, count + 1);
                }
            }
        }
    }

    static int[][] getLetters() {
        int[][] letters = new int[26][2];
        for (int i = 2, let = 0; i < lettersInDigits.length; i++)
            for (int j = 1; j <= lettersInDigits[i]; j++)
                letters[let++] = new int[]{i, j};
        return letters;
    }

}