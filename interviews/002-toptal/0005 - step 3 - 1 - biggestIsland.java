// Find the biggest island of 1's in a nxn matrix which  contains only 0s and 1s

public static int findBiggest(int[][] matrix) {
    int biggest = 0;
    int[][] temp = new int[matrix.length][matrix[0].length];
    for (int i = 0; i < matrix.length; i++) {
        for (int j = 0; j < matrix[0].length; j++) {
            if (matrix[i][j] == 1) {

                if (i != 0 && matrix[i - 1][j] > 0) {
                    matrix[i - 1][j]++;
                    matrix[i][j] = matrix[i-1][j];
                }

                if (j != 0 && matrix[i][j - 1] > 0) {
                    matrix[i][j - 1]++;
                    matrix[i][j] = matrix[i][j - 1];
                }

                if (matrix[i][j] > biggest) biggest = matrix[i][j];
            }
        }
    }

    return biggest;
}
