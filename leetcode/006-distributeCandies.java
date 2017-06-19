public int distributeCandies(int[] candies) {
    Arrays.sort(candies);
    int sister = 1;
    int kind = candies[0];
    int i = 1;
    while(i < candies.length) {
        if(kind != candies[i]) {
            sister++;
            kind = candies[i];
        }
        i++;
    }

    if(sister > candies.length/2) return candies.length/2;
    return sister;
}
