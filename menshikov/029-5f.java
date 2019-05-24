import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f5_1();
    }

    static void f5_1() {
        int bDay = sc.nextInt(), bMonth = sc.nextInt(),
                thisDay = sc.nextInt(), thisMon = sc.nextInt(), thisYear = sc.nextInt();

        int[] days = new int[] {0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
        int res = 0, monthDays;
        while (thisDay != bDay || thisMon != bMonth) {
            if (thisMon == 2 && (thisYear % 400 == 0 || (thisYear % 4 == 0 && thisYear % 100 != 0))) monthDays = 29;
            else monthDays = days[thisMon];

            if (thisMon == 12 && thisDay == 31) {
                thisYear++;
                thisMon = 1;
                thisDay = 1;
            } else if (thisDay == monthDays) {
                thisMon++;
                thisDay = 1;
            } else thisDay++;
            res++;
        }

        System.out.println(res);
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