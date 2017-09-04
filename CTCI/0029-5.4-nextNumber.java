static void nextNumber(int num) {
    int ones = countOnes(num);
    System.out.println(findSmallest(num, ones));
    System.out.println(findLargest(num, ones));
}

static int countOnes(int num) {
    int ones = 0;
    while (num != 0) {
        if ((num & 1) == 1) ones++;
        num >>>= 1;
    }
    return ones;
}

static int findLargest(int num, int ones) {
    int largestOnes;
    do {
        largestOnes = countOnes(++num);
    } while (largestOnes != ones);
    return num;
}

static int findSmallest(int num, int ones) {
    int smallestOnes;
    do {
        smallestOnes = countOnes(--num);
    } while (smallestOnes != ones);
    return num;
}
