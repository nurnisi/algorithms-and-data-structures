import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        c7();
    }

    static int len = 0;
    static long N;
    static long[] nums = new long[7000];

    static void c7() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        N = sc.nextLong();
        int i = 0;
        nums[i] = 1;

        //находим все игровые позиции
        while (i <= len) {
            for (int j = 2; j <= 9; j++)
                insert(nums[i] * j);
            i++;
        }

        //вычисляем выигрышность каждый позиции
        boolean[] wins = new boolean[len + 1];
        for (int j = len; j >= 0; j--) {
            if (nums[j] * 9 >= N) {
                wins[j] = true;
                continue;
            }
            for (int k = 2; k <= 9; k++)
                if (!wins[indexOf(nums[j] * k)]) {
                    wins[j] = true;
                    break;
                }
        }

        pw.println(wins[0] ? "Stan wins." : "Ollie wins.");
        pw.close();
    }

    static int indexOf(long n) {
        int l = 0, mid, r = len;
        while (l <= r) {
            mid = (l + r)/2;
            if (n == nums[mid]) return mid;
            if (nums[mid] < n) l = mid + 1;
            else r = mid - 1;
        }
        return -1;
    }

    static void insert(long n) {
        if (n > N || indexOf(n) != -1) return;

        int i = len;
        while (i >= 0 && nums[i] > n) nums[i + 1] = nums[i--];
        nums[i + 1] = n;
        len++;
    }
}