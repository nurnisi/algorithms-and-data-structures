import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        e7();
    }

    static void e7() throws IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int N = sc.nextInt();
        int ball = 0, wall = -3, empty = -1, rowBall = 0, colBall = 0, rowDest = 0, colDest = 0;
        char cBall = '@', cWall = 'O', cDest = 'X', cEmpty = '.';
        int[][] arr = new int[N + 2][N + 2];

        //define walls
        for (int i = 0; i < N + 2; i++) {
            arr[0][i] = wall;
            arr[i][0] = wall;
            arr[N + 1][i] = wall;
            arr[i][N + 1] = wall;
        }

        //read input matrix
        for (int i = 1; i <= N; i++) {
            String line = sc.next();
            for (int j = 1; j <= N; j++) {
                char ch = line.charAt(j - 1);
                if (ch == cEmpty) arr[i][j] = empty;
                else if (ch == cWall) arr[i][j] = wall;
                else if (ch == cDest) {
                    arr[i][j] = empty;
                    rowDest = i;
                    colDest = j;
                }
                else {
                    arr[i][j] = ball;
                    rowBall = i;
                    colBall = j;
                }
            }
        }

        //BFS
        Queue<int[]> queue = new LinkedList<>();
        queue.add(new int[]{rowBall, colBall});
        int[][] dirs = new int[][]{{-1,0},{0,-1},{1,0},{0,1}};
        while (!queue.isEmpty()) {
            int[] cur = queue.poll();
            for (int[] d : dirs) {
                int r = cur[0] + d[0], c = cur[1] + d[1];
                if (arr[r][c] == empty) {
                    arr[r][c] = arr[cur[0]][cur[1]] + 1;
                    queue.add(new int[]{r, c});
                }
            }
        }

        if (arr[rowDest][colDest] == empty) pw.print("N");
        else {
            //build path
            int path = -4, cur = arr[rowDest][colDest];
            arr[rowDest][colDest] = path;
            while (rowDest != rowBall || colDest != colBall) {
                for (int[] d : dirs) {
                    int r = rowDest + d[0], c = colDest + d[1];
                    if (arr[r][c] == cur - 1) {
                        arr[r][c] = path;
                        rowDest = r;
                        colDest = c;
                        cur--;
                        break;
                    }
                }
            }

            //print answer
            pw.println("Y");
            char cPath = '+';
            arr[rowBall][colBall] = ball;
            for (int i = 1; i < N + 1; i++) {
                for (int j = 1; j < N + 1; j++) {
                    int k = arr[i][j];
                    if (k == path) pw.print(cPath);
                    else if (k == wall) pw.print(cWall);
                    else if (k == ball) pw.print(cBall);
                    else pw.print(cEmpty);
                }
                pw.println();
            }
        }

        pw.close();
    }
}