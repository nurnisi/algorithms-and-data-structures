import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(maxAreaOfIsland(new int[][]{{0,1,1,1,1,1},
                                                       {0,1,0,0,0,1},
                                                       {0,1,1,1,0,1}}));
    }

    static int row, col;

    public static int maxAreaOfIsland(int[][] grid) {
        int max = 0;
        row = grid.length; col = grid[0].length;
        boolean[][] visited = new boolean[row][col];
        for (int i = 0; i < row; i++)
            for (int j = 0; j < col; j++)
                max = Math.max(helper(visited, grid, i, j), max);

        return max;
    }

    public static int helper(boolean[][] visited, int[][] grid, int i, int j) {
        if (grid[i][j] == 0 || visited[i][j]) return 0;
        else {
            visited[i][j] = true;
            return 1 + (i > 0 ? helper(visited, grid, i - 1, j) : 0)
                     + (i < row - 1? helper(visited, grid, i + 1, j) : 0)
                     + (j > 0 ? helper(visited, grid, i, j - 1) : 0)
                     + (j < col - 1? helper(visited, grid, i, j + 1) : 0);
        }
    }
}
