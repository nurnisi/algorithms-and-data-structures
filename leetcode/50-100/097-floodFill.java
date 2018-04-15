import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        floodFill(new int[][]{{0,0,0}
                             ,{0,0,0}},0,0,2);
    }

    public static int[][] floodFill(int[][] image, int sr, int sc, int newColor) {
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