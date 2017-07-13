public static int[][] zeroMatrix(int[][] matrix) {
    if (matrix.length == 0 || matrix[0].length == 0) return  matrix;

    Set<Integer> rows = new HashSet<>();
    Set<Integer> cols = new HashSet<>();

    for (int i = 0; i < matrix.length; i++)
        for (int j = 0; j < matrix[0].length; j++)
            if (matrix[i][j] == 0) {
                if (!rows.contains(i)) rows.add(i);
                if (!cols.contains(j)) cols.add(j);
            }

    for (int i = 0; i < matrix.length; i++)
        for (int j = 0; j < matrix[0].length; j++)
            if (rows.contains(i) || cols.contains(j)) matrix[i][j] = 0;

    return matrix;
}
