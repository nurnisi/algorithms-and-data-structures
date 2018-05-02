public class leetcode {

    public static void main(String[] args) {
        System.out.println(largestTriangleArea(new int[][]{{1,0},{0,0},{0,1}}));
    }

    static double maxArea = Double.MIN_VALUE;

    public static double largestTriangleArea(int[][] points) {
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
