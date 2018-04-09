public int maxCount(int m, int n, int[][] ops) {
    if(ops.length == 0) return m * n;
    int k = Integer.MAX_VALUE, l = k;
    for (int i = 0; i < ops.length; i++) {
        k = Math.min(ops[i][0], k);
        l = Math.min(ops[i][1], l);
    }
    return k * l;
}
