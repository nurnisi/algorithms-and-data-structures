import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        a8_2();
    }

    static int[] arr;
    static Set<Long> set;

    static void a8_2() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = sc.nextInt();
        Arrays.sort(arr);

        long sum = 0;
        for (int i : arr) {
            if (sum + 1 >= i) sum += i;
            else break;
        }

        pw.println(sum + 1);
        pw.close();
    }

    //my solution: time limit exceeded
    static void a8() throws  IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        arr = new int[N];
        for (int i = 0; i < N; i++) arr[i] = sc.nextInt();
        Arrays.sort(arr);

        set = new TreeSet<>();

        helper(0, 0);

        long i = 1;
        for (long n : set) {
            if (i != n)
                break;
            i++;
        }

        pw.println(i);
        pw.close();
    }

    static void helper(int cur, long sum) {
        if (cur == arr.length) return;
        for (int i = cur; i < arr.length; i++) {
            set.add(sum + arr[i]);
            helper(i + 1, sum + arr[i]);
        }
    }

}