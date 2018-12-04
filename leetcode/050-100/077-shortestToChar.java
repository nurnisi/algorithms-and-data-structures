public static int[] shortestToChar(String S, char C) {
    int len = S.length();
    int[] res = new int[len];

    int prev = Integer.MIN_VALUE / 2;
    for (int i = 0; i < len; i++) {
        if (S.charAt(i) == C) prev = i;
        res[i] = i - prev;
    }

    prev = Integer.MAX_VALUE / 2;
    for (int i = len - 1; i >= 0; i--) {
        if (S.charAt(i) == C) prev = i;
        res[i] = Math.min(res[i], prev - i);
    }

    return res;
}


public static int[] shortestToChar(String S, char C) {
    List<Integer> indexes = new ArrayList<>();
    int slen = S.length();
    for (int i = 0; i < slen; i++)
        if (S.charAt(i) - C == 0)
            indexes.add(i);

    int[] res = new int[slen];
    int first = indexes.get(0), last = indexes.get(indexes.size() - 1);
    for (int i = 0; i < first; i++) res[i] = first - i;
    for (int i = 0; i < indexes.size() - 1; i++) {
        int left = indexes.get(i), right = indexes.get(i + 1), mid = (left + right) / 2;
        for (int j = left + 1; j < right; j++) {
            res[j] = j <= mid ? j - left : right - j;
        }
    }
    for (int i = last + 1; i < slen; i++)
        res[i] = i - last;

    return res;
}