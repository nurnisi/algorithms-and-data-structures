public static int[][] rotateMatrix(int[][] matrix) {
    int l = matrix.length;
    int[][] rotate = new int[l][l];
    for (int i = 0, k = l - 1; i < l; i++, k--)
        for (int j = 0; j < l; j++)
            rotate[j][k] = matrix[i][j];
    return rotate;
}
