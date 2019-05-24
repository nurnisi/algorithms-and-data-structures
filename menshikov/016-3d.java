import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        d3_3();
    }

    //can not pass some tests
    static void d3_3() {
        int a = sc.nextInt(),
                b = sc.nextInt(),
                c = sc.nextInt(),
                d = sc.nextInt();

        int widthO = a > b ? a : b,
                heightO = a < b ? a : b,
                widthK = c > d ? c : d,
                heightK = c < d ? c : d;

        if (heightO > heightK) System.out.println("Impossible");
        else {
            if (widthO <= widthK) System.out.println("Possible");
            else {
                double angle = 2 * Math.atan2(heightO, widthO);

                double BO = Math.sqrt(Math.pow(heightO, 2) + Math.pow(widthO, 2)) / 2;
                double AB = Math.sqrt(Math.pow(heightK / 2, 2) + Math.pow(BO, 2));
                double AOB = Math.atan2(AB, heightK / 2);
                double CD = Math.sqrt(Math.pow(widthK / 2, 2) + Math.pow(BO, 2));
                double COD = Math.atan2(CD, widthK / 2);
                double BOC = 90 - AOB - COD;

                if (angle <= BOC) System.out.println("Possible");
                else System.out.println("Impossible");
            }
        }
    }

    //can not pass some tests
    static void d3_2() {
        int a = sc.nextInt(),
                b = sc.nextInt(),
                c = sc.nextInt(),
                d = sc.nextInt();

        int widthO = a > b ? a : b,
                heightO = a < b ? a : b,
                widthK = c > d ? c : d,
                heightK = c < d ? c : d;

        if (heightO > heightK) System.out.println("Impossible");
        else {
            if (widthO <= widthK) System.out.println("Possible");
            else {
                double AC = Math.sqrt(Math.pow(widthO, 2) + Math.pow(heightO, 2));
                double CF = Math.sqrt(Math.pow(AC, 2) + Math.pow(heightK, 2));
                double CAB = Math.atan2(heightO, widthO);
                double FAC = Math.atan2(CF, heightK);
                double BAE = 90 - (CAB + FAC);
                double GE = heightO * Math.sin(BAE) + widthO * Math.cos(BAE);
                if (GE <= widthK) System.out.println("Possible");
                else System.out.println("Impossible");
            }
        }

    }

    static void d3() {
        int a = sc.nextInt(),
                b = sc.nextInt(),
                c = sc.nextInt(),
                d = sc.nextInt();

        int max1 = a > b ? a : b,
                min1 = a < b ? a : b,
                max2 = c > d ? c : d,
                min2 = c < d ? c : d;

        if (max1 <= max2 && min1 <= min2) System.out.println("Possible");
        else {
            double diag = Math.sqrt(Math.pow(max2, 2) + Math.pow(min2, 2));
            if (diag - min1 >= max1) System.out.println("Possible");
            else System.out.println("Impossible");
        }


    }
}