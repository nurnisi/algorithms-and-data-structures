import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        d2();
    }

    static class Point {
        public int x;
        public int y;
        public Point (int x, int y) {
            this.x = x;
            this.y = y;
        }
    }

    static void d2() {
        Point p1 = new Point(sc.nextInt(), sc.nextInt());
        Point p2 = new Point(sc.nextInt(), sc.nextInt());
        Point p3 = new Point(sc.nextInt(), sc.nextInt());
        Point p4 = new Point(sc.nextInt(), sc.nextInt());

        if (lineEquation(p1, p2, p3) == 0 && lineEquation(p1, p2, p4) == 0) {
            if (isIn(p1, p2, p3) || isIn(p1, p2, p4)) System.out.println("Yes");
            else System.out.println("No");
        } else if (lineEquation(p1, p2, p3) * lineEquation(p1, p2, p4) > 0
                || lineEquation(p3, p4, p1) * lineEquation(p3, p4, p2) > 0) {
            System.out.println("No");
        } else {
            System.out.println("Yes");
        }
    }

    static long lineEquation(Point p1, Point p2, Point p) {
        return (p.x * (p1.y - p2.y) + p.y * (p2.x - p1.x) + p1.x * p2.y - p2.x * p1.y);
    }

    static boolean isIn (Point p1, Point p2, Point p) {
        return (p1.x <= p.x && p.x <= p2.x && p1.y <= p.y && p.y <= p2.y)
                || (p2.x <= p.x && p.x <= p1.x && p2.y <= p.y && p.y <= p1.y);
    }
}