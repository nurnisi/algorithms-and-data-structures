import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(maxAreaOfIsland(new int[][]{{0,1,1,1,1,1},
                                                       {0,1,0,0,0,1},
                                                       {0,1,1,1,0,1}}));
    }

    //leetcode solutin: DFS iterative
    public static int maxAreaOfIsland(int[][] grid) {
        boolean[][] visited = new boolean[grid.length][grid[0].length];
        int[] dr = new int[]{-1,1,0,0};
        int[] dc = new int[]{0,0,-1,1};

        int ans = 0;
        for (int r0 = 0; r0 < grid.length; r0++)
            for (int c0 = 0; c0 < grid[0].length; c0++)
                if (grid[r0][c0] == 1 && !visited[r0][c0]) {
                    int shape = 0;
                    Stack<int[]> stack = new Stack<>();
                    stack.push(new int[]{r0,c0});
                    visited[r0][c0] = true;
                    while (!stack.isEmpty()) {
                        int[] node = stack.pop();
                        int r = node[0], c = node[1];
                        shape++;
                        for (int k = 0; k < 4; k++) {
                            int nr = r + dr[k], nc = c + dc[k];
                            if (nr >= 0 && nr < grid.length &&
                                    nc >= 0 && nc < grid[0].length &&
                                    grid[nr][nc] == 1 && !visited[nr][nc]) {
                                stack.push(new int[]{nr,nc});
                                visited[nr][nc] = true;
                            }
                        }
                    }
                    ans = Math.max(ans, shape);
                }

        return ans;
    }

    //leetcode solution: more understandable DFS recursive
    static int[][] grid;
    static boolean[][] visited;

    public static int maxAreaOfIsland3(int[][] grid) {
        int max = 0;
        leetcode.grid = grid;
        visited = new boolean[grid.length][grid[0].length];
        for (int i = 0; i < grid.length; i++)
            for (int j = 0; j < grid[0].length; j++)
                max = Math.max(helper(i, j), max);

        return max;
    }

    public static int helper(int i, int j) {
        if (i < 0 || i >= grid.length ||
            j < 0 || j >= grid[0].length ||
            grid[i][j] == 0 || visited[i][j]) return 0;

        visited[i][j] = true;
        return 1 + helper(i - 1, j) + helper(i + 1, j)
                 + helper(i, j - 1) + helper(i, j + 1);
    }

    //my solution: DFS recursive
    static int row, col;

    public static int maxAreaOfIsland2(int[][] grid) {
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
