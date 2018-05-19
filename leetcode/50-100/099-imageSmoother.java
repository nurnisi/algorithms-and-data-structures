import java.util.*;

public class leetcode {

    public static void main(String[] args) {
    }

    public static int[][] imageSmoother(int[][] M) {
        int[][] ans = new int[M.length][M[0].length];
        int[][] dir = new int[][]{{0,0}, {-1,0}, {-1,-1}, {0,-1}, {1,-1}, {1,0}, {1,1}, {0,1}, {-1,1}};
        for (int i = 0; i < M.length; i++) {
            for (int j = 0; j < M[0].length; j++) {
                int sum = 0, count = 0;
                for (int[] d : dir) {
                    int r = i + d[0], c = j + d[1];
                    if (r >= 0 && r < M.length && c >=0 && c < M[0].length) {
                        sum += M[r][c];
                        count++;
                    }
                    ans[i][j] = sum / count;
                }
            }
        }
        return ans;
    }
}