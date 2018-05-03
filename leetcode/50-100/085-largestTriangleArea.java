public class leetcode {

    public static void main(String[] args) {
        System.out.println(largestTriangleArea(new int[][]{{-35,19},{40,19},{27,-20},{35,-3},{44,20},{22,-21},{35,33},{-19,42},{11,47},{11,37}}));
    }

    //solution by Law of Cosines
    //angleC = Math.acos((a*a + b*b - c*c) / 2*a*b)
    //Area = 0.5 * a * b * Math.sin(angleC)
    public static double areaByLawOfCosines(int[] p1, int[] p2, int[] p3) {
        double  a = getDistance(p1, p2),
                b = getDistance(p2, p3),
                c = getDistance(p1, p3),
                acos = (a*a + b*b - c*c) / (2*a*b),
                angleC = 0;
        if (acos > -1 && acos < 1) angleC = Math.acos(acos);
        return 0.5 * a * b * Math.sin(angleC);
    }

    //solution by Heron's formula
    //s = (a + b + c) / 2
    //Area = Math.sqrt(s * (s-a) * (s-b) * (s-c))
    public static double areaByHeronsFormula(int[] p1, int[] p2, int[] p3) {
        double  d1 = getDistance(p1, p2),
                d2 = getDistance(p2, p3),
                d3 = getDistance(p1, p3),
                s = (d1 + d2 + d3) / 2,
                check = s * (s - d1) * (s - d2) * (s - d3);
        if (check > 0) return Math.sqrt(check);
        return 0;
    }

    public static double getDistance(int[] a, int[] b) {
        int x1 = a[0], y1 = a[1], x2 = b[0], y2 = b[1];
        return Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
    }

    //solution by shoelace formula
    //Area = 1/2 * Math.abs(x1*y2 + x2*y3 + x3*y1 - x2*y1 - x3*y2 - x1*y3)
    public static double largestTriangleArea(int[][] points) {
        int N = points.length;
        double ans = 0;
        for (int i = 0; i < N; i++)
            for (int j = i+1; j < N; j++)
                for (int k = j+1; k < N; k++)
                    ans = Math.max(ans, areaByLawOfCosines(points[i], points[j], points[k]));

        return ans;
    }

    public static double areaBySholaceFormula(int[] p1, int[] p2, int[] p3) {
        return 0.5 * Math.abs(p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]
                            - p2[0]*p1[1] - p3[0]*p2[1] - p1[0]*p3[1]);
    }

    //my solution - failing tests
    static double maxArea = Double.MIN_VALUE;

    public static double largestTriangleArea2(int[][] points) {
        double[][] d = getDistances(points);
        areaRecursively(new int[3], 0, d, 0);
        return maxArea;
    }

    public static double[][] getDistances(int[][] points) {
        double[][] distances = new double[points.length][points.length];
        for (int i = 0; i < points.length; i++) {
            for (int j = i + 1; j < points.length; j++) {
                double d = getd(points[i], points[j]);
                distances[i][j] = d;
                distances[j][i] = d;
            }
        }
        return distances;
    }

    public static double getd(int[] a, int[] b) {
        int x1 = a[0], y1 = a[1], x2 = b[0], y2 = b[1];
        return Math.sqrt(Math.pow((x2 - x1), 2) + Math.pow((y2 - y1), 2));
    }

    public static void areaRecursively(int[] curPoints, int cur, double[][] distances, int index) {
        if (cur == curPoints.length) {
            double  d1 = distances[curPoints[0]][curPoints[1]],
                    d2 = distances[curPoints[1]][curPoints[2]],
                    d3 = distances[curPoints[0]][curPoints[2]],
                    p = (d1 + d2 + d3) / 2,
                    area = Math.sqrt(p * (p - d1) * (p - d2) * (p - d3));
            maxArea = Math.max(area, maxArea);
        } else {
            for (int i = index; i < distances.length; i++) {
                curPoints[cur] = i;
                areaRecursively(curPoints, cur + 1, distances, i + 1);
            }
        }
    }
}
