import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(isToeplitzMatrix(new int[][]{{1,2,3,4},{5,1,2,3},{9,5,1,2}}));
    }

    public static boolean isToeplitzMatrix(int[][] matrix) {
        Map<Integer, Integer> map = new HashMap<>();
        for (int row = 0; row < matrix.length; row++)
            for (int col = 0; col < matrix[0].length; col++) {
                if (!map.containsKey(row - col))
                    map.put(row - col, matrix[row][col]);
                else if (map.get(row - col) != matrix[row][col])
                    return false;
            }

        return true;
    }

    public static boolean isToeplitzMatrix2(int[][] matrix) {
        for (int i = 1; i < matrix.length; i++)
            for (int j = 1; j < matrix[0].length; j++)
                if (matrix[i][j] != matrix[i - 1][j - 1]) return false;

        return true;
    }
}
