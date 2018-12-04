import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        floodFill(new int[][]{{0,0,0}
                             ,{0,1,1}},1,1,1);
    }

    //iterative: DFS
    public static int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
        int color = image[sr][sc];
        if (color == newColor) return image;
        Stack<int[]> stack = new Stack<>();
        stack.add(new int[]{sr,sc});

        while (!stack.isEmpty()) {
            int[] cur = stack.pop();
            if (image[cur[0]][cur[1]] == color) {
                image[cur[0]][cur[1]] = newColor;
                if (cur[0] - 1 >= 0) stack.add(new int[]{cur[0] - 1, cur[1]});
                if (cur[0] + 1 < image.length) stack.add(new int[]{cur[0] + 1, cur[1]});
                if (cur[1] - 1 >= 0) stack.add(new int[]{cur[0], cur[1] - 1});
                if (cur[1] + 1 < image[0].length) stack.add(new int[]{cur[0], cur[1] + 1});
            }
        }
        return image;
    }

    //recursive: DFS
    public static int[][] floodFill3(int[][] image, int sr, int sc, int newColor) {
        if (image[sr][sc] == newColor) return image;
        dfs(image, sr, sc, newColor, image[sr][sc]);
        return image;
    }

    public static void dfs(int[][] image, int sr, int sc, int newColor, int color) {
        if (sr < 0 || sr >= image.length || sc < 0 || sc >= image[0].length || image[sr][sc] != color) return;
        image[sr][sc] = newColor;
        dfs(image, sr + 1, sc, newColor, color);
        dfs(image, sr - 1, sc, newColor, color);
        dfs(image, sr, sc + 1, newColor, color);
        dfs(image, sr, sc - 1, newColor, color);
    }

    //iterative: BFS
    public static int[][] floodFill2(int[][] image, int sr, int sc, int newColor) {
        boolean[][] visited = new boolean[image.length][image[0].length];
        int[] dr = new int[]{-1,1,0,0};
        int[] dc = new int[]{0,0,-1,1};
        int color = image[sr][sc];
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{sr,sc});

        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            image[cur[0]][cur[1]] = newColor;
            visited[cur[0]][cur[1]] = true;

            for (int i = 0; i < 4; i++) {
                int row = cur[0] + dr[i], col = cur[1] + dc[i];
                if (row >= 0 && row < image.length
                        && col >= 0 && col < image[0].length
                        && !visited[row][col] && image[row][col] == color)
                    queue.add(new int[]{row,col});
            }
        }
        return image;
    }
}