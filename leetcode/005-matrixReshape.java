public int[][] matrixReshape(int[][] nums, int r, int c) {
    int rows = nums.length;
    int cols = nums[0].length;
    if(rows * cols != r * c) return nums;

    int[] temp = new int[rows * cols];
    int k = 0;
    for(int i = 0; i < rows; i++) {
        for(int j = 0; j < cols; j++) {
            temp[k++] = nums[i][j];
        }
    }

    int[][] reshape = new int[r][c];
    int l = 0;
    for(int m = 0; m < r; m++) {
        for(int n = 0; n < c; n++) {
            reshape[m][n] = temp[l++];
        }
    }

    return reshape;
}
