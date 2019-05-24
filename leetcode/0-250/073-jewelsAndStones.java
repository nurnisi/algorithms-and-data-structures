public static int numJewelsInStones(String J, String S) {
    boolean[] arr = new boolean[58];
    for (char ch : J.toCharArray()) {
        arr[ch - 'A'] = true;
    }

    int count = 0;
    for (char ch : S.toCharArray()) {
        if (arr[ch - 'A']) count++;
    }

    return count;
}