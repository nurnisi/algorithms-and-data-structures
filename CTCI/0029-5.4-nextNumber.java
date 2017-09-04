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

//CTCI: getNext
static int getNext(int num) {
    int c = num, c0 = 0, c1 = 0;
    while ((c & 1) == 0 && c != 0) {
        c0++;
        c >>= 1;
    }

    while ((c & 1) == 1) {
        c1++;
        c >>= 1;
    }

    if (c0 + c1 == 32 || c0 + c1 == 0) return -1;

    int p = c0 + c1;
    num |= (1 << p);
    num &= ~((1 << p) - 1);
    num |= ((1 << (c1 - 1)) - 1);

    return num;
}

//CTCI: getPrev
static int getPrev(int num) {
    int c = num, c0 = 0, c1 = 0;
    while ((c & 1) == 1 && c != 0) {
        c1++;
        c >>= 1;
    }

    if (c == 0) return -1;

    while ((c & 1) == 0 && c != 0) {
        c0++;
        c >>= 1;
    }

    int p = c0 + c1;
    num &= ((~0) << (p + 1));
    int mask = (1 << (c1 + 1)) - 1;
    num |= mask << (c0 - 1);

    return num;
}

//CTCI: 
static int getNextArithmetic(int num) {
    int c = num, c0 = 0, c1 = 0;
    while ((c & 1) == 0 && c != 0) {
        c0++;
        c >>= 1;
    }

    while ((c & 1) == 1) {
        c1++;
        c >>= 1;
    }

    if (c0 + c1 == 31 || c0 + c1 == 0) return -1;

    return num + (1 << c0) + (1 << (c1 - 1)) - 1;
}
