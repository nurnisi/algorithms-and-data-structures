import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f5();
    }

    static void f5() {
        int day1 = sc.nextInt(), month1 = sc.nextInt(),
                day2 = sc.nextInt(), month2 = sc.nextInt(), year2 = sc.nextInt();

        int[] ds = new int[] {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int res = 0;
        while (month2 != month1) {
            if (month2 > 12) {
                month2 = 1;
                year2++;
            }
            if (month2 == 2 && (year2 % 400 == 0 || (year2 % 4 == 0 && year2 % 100 != 0))) res++;
            res += ds[month2++];
        }
        if (day1 == 29 && month1 == 2) {
            while (year2 % 400 != 0 && year2 % 4 != 0) {
                year2++;
                res += 365;
            }
        }
        res += day1 - day2;
        System.out.println(res);
    }
}