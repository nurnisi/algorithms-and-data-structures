import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(isToeplitzMatrix(new int[][]{{1,2},{2,2}}));
    }

    public static boolean isToeplitzMatrix(int[][] matrix) {
        for (int i = 1; i < matrix.length; i++)
            for (int j = 1; j < matrix[0].length; j++)
                if (matrix[i][j] != matrix[i - 1][j - 1]) return false;

        return true;
    }
}
