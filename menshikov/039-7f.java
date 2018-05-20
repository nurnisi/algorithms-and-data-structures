import java.io.*;
import java.util.*;

public class acmp {

    static PrintWriter pw;
    static Scanner sc;

    public static void main(String[] args) throws IOException {
        f7();
    }

    //global variables to overcome Memory limit
    static char[][] arr;
    static int ii, jj;

    static void f7() throws  IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        int M = sc.nextInt(), N = sc.nextInt();
        arr = new char[M + 2][N + 2];
        //initialize borders
        for (int i = 0; i < M + 2; i++) {
            arr[i][0] = '.';
            arr[i][N + 1] = '.';
        }
        for (int j = 0; j < N + 2; j++) {
            arr[0][j] = '.';
            arr[M + 1][j] = '.';
        }

        //read input matrix
        for (int i = 1; i < M + 1; i++) {
            String line = sc.next();
            for (int j = 1; j < N + 1; j++) {
                arr[i][j] = line.charAt(j - 1);
            }
        }

        //recursive DFS
        int count = 0;
        for (ii = 1; ii < M + 1; ii++) {
            for (jj = 1; jj < N + 1; jj++) {
                if (arr[ii][jj] == '#') {
                    count++;
                    recursion();
                }
            }
        }

        pw.println(count);
        pw.close();
    }

    static void recursion() {
        if (arr[ii][jj] != '#') return;
        arr[ii][jj] = '.';

        ii--;
        recursion();
        ii++;

        ii++;
        recursion();
        ii--;

        jj--;
        recursion();
        jj++;

        jj++;
        recursion();
        jj--;
    }

    //my solution: memory limit exceeded
    static void f7_2() throws  IOException {
        sc = new Scanner(new File("input.txt"));
        pw = new PrintWriter(new File("output.txt"));

        byte M = sc.nextByte(), N = sc.nextByte();
        byte[][] arr = new byte[M][N];
        for (byte i = 0; i < M; i++) {
            String line = sc.next();
            for (byte j = 0; j < N; j++) {
                arr[i][j] = (byte) line.charAt(j);
            }
        }

        Queue<byte[]> queue = new LinkedList<>();
        byte[][] dirs = new byte[][]{{-1,0},{0,-1},{1,0},{0,1}};
        short count = 0;
        for (byte i = 0; i < M; i++) {
            for (byte j = 0; j < N; j++) {
                if (arr[i][j] == 35) {
                    count++;
                    queue.add(new byte[]{i,j});
                    while (!queue.isEmpty()) {
                        byte[] cur = queue.poll();
                        arr[cur[0]][cur[1]] = 40;
                        for (byte[] d : dirs) {
                            byte r = (byte) (cur[0] + d[0]), c = (byte) (cur[1] + d[1]);
                            if (r >= 0 && r < M && c >= 0 && c < N && arr[r][c] == 35)
                                queue.add(new byte[]{r,c});
                        }
                    }
                }
            }
        }

        pw.println(count);
        pw.close();
    }
}