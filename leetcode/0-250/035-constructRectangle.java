public static int[] constructRectangle(int area) {
    int n = (int) Math.sqrt(area);
    while(area % n != 0) n--;
    return new int[]{area/n, n};
}
