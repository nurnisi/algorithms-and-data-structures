public int hammingDistance(int x, int y) {
    int res = 0;
    for(int i=0; i<32; i++) {
        if(((x>>i) & 1) != ((y>>i) & 1)) res++;
    }
    return res;
}
