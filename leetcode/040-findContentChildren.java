//mine
public static int findContentChildren(int[] g, int[] s) {
    Arrays.sort(g);
    Arrays.sort(s);
    int res = 0, j = 0;
    for (int i = 0; i < g.length; i++) {
        while(j < s.length && s[j] < g[i]) j++;
        if(j >= s.length) break;
        if(g[i] <= s[j]) {
            res++;
            j++;
        }
    }
    return res;
}

//refractored
public static int findContentChildren(int[] g, int[] s) {
    Arrays.sort(g);
    Arrays.sort(s);
    int i = 0;
    for (int j = 0; i< g.length && j < s.length; j++) {
        if(g[i] <= s[j]) i++;
    }
    return i;
}
