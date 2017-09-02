public static int flipBitToWin(int num) {
    int c1 = 0, c2 = 0, zeros = 0, max = Integer.MIN_VALUE;
    for (int i = 0; i < 32; i++) {
        if ((num & 1) == 0) {
            zeros++;
            if (c2 != 0) {
                max = Math.max(max, c1 + c2 + 1);
                c1 = c2;
                c2 = 0;
                zeros = 1;
            } else if (zeros > 1) {
                max = Math.max(max, c1 + 1);
                c1 = 0;
            }
        } else {
            if (c1 == 0) zeros = 0;
            if (zeros == 0) c1++;
            else if (zeros == 1) c2++;
        }
        num >>= 1;
    }
    return max;
}

//CTCI: brute force
static int longestSequence(int n) {
    if (n == -1) return Integer.BYTES * 8;
    List<Integer> sequences = getAlternatingSequences(n);
    return findLongestSequence(sequences);
}

static List<Integer> getAlternatingSequences(int n) {
    List<Integer> sequences = new ArrayList<>();

    int searchingFor = 0, counter = 0;
    for (int i = 0; i < Integer.BYTES * 8; i++) {
        if ((n & 1) != searchingFor) {
            sequences.add(counter);
            searchingFor = n & 1;
            counter = 0;
        }
        counter++;
        n >>= 1;
    }
    sequences.add(counter);

    return sequences;
}

static int findLongestSequence(List<Integer> sequences) {
    int maxSeq = 1;

    for (int i = 0; i < sequences.size(); i += 2) {
        int zeroSeq = sequences.get(i);
        int onesSeqLeft = i - 1 >= 0 ? sequences.get(i - 1) : 0;
        int onesSeqRight = i + 1 < sequences.size() ? sequences.get(i + 1) : 0;

        int thisSeq = 0;
        if (zeroSeq == 1) thisSeq = onesSeqLeft + onesSeqRight + 1;
        else if (zeroSeq > 1) thisSeq = 1 + Math.max(onesSeqLeft, onesSeqRight);
        else if (zeroSeq == 0) thisSeq = Math.max(onesSeqLeft, onesSeqRight);

        maxSeq = Math.max(maxSeq, thisSeq);
    }

    return maxSeq;
}