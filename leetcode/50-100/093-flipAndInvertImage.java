import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(flipAndInvertImage(new int[][]{{1,1,0,0},{1,0,0,1},{0,1,1,1},{1,0,1,0}}));
    }

    public static int[][] flipAndInvertImage(int[][] A) {
        int col = A[0].length;
        for (int[] row : A)
            for (int i = 0; i < (col + 1) / 2; i++) {
                int temp = row[i];
                row[i] = row[col - i - 1] ^ 1;
                row[col - i - 1] = temp ^ 1;
            }
        return A;
    }

    public static int[][] flipAndInvertImage2(int[][] A) {
        for (int i = 0; i < A.length; i++) {
            for (int j = 0; j < Math.ceil(((double)A[0].length) / 2); j++) {
                int temp = A[i][j];
                A[i][j] = A[i][A[0].length - j - 1] ^ 1;
                A[i][A[0].length - j - 1] = temp ^ 1;
            }
        }
        return A;
    }
}