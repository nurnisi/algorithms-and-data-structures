public static int[][] rotateMatrix(int[][] matrix) {
    int l = matrix.length;
    int[][] rotate = new int[l][l];
    for (int i = 0, k = l - 1; i < l; i++, k--)
        for (int j = 0; j < l; j++)
            rotate[j][k] = matrix[i][j];
    return rotate;
}

//in place from ctci
public static int[][] rotateMatrix(int[][] matrix) {
    int n = matrix.length;
    for (int layer = 0; layer < n / 2; layer++) {
        int first = layer;
        int last = n - 1 - layer;
        for (int i = first; i < last; i++) {
            int offset = i - first;
            int top = matrix[first][i];
            matrix[first][i] = matrix[last - offset][first];
            matrix[last - offset][first] = matrix[last][last - offset];
            matrix[last][last - offset] = matrix[i][last];
            matrix[i][last] = top;
        }
    }
    return matrix;
}
