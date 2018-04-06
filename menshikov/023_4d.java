import java.util.*;
import java.math.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        d4();
    }

    static void d4() {
        int n = sc.nextInt(),
                x1 = sc.nextInt(),
                y1 = sc.nextInt(),
                prevX = x1,
                prevY = y1,
                nextX, nextY;

        double area = 0;

        for (int i = 1; i < n; i++) {
            nextX = sc.nextInt();
            nextY = sc.nextInt();

            area += ((prevX - nextX) * (prevY + nextY));

            prevX = nextX;
            prevY = nextY;
        }

        area += ((prevX - x1) * (prevY + y1));
        area /= 2;
        area = Math.abs(area);
        area = round(area, 1);
        System.out.print(area);
    }

    public static double round(double value, int places) {
        if (places < 0) throw new IllegalArgumentException();

        BigDecimal bd = new BigDecimal(value);
        bd = bd.setScale(places, RoundingMode.HALF_UP);
        return bd.doubleValue();
    }
}