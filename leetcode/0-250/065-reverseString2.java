public static String reverseStr (String s, int k) {
    char[] arr = s.toCharArray();
    int i = 0, tempK;
    while (i < arr.length) {
        int j = i;
        tempK = j + k - 1;
        if (tempK >= arr.length) tempK = arr.length - 1;
        while (j < tempK) {
            swap(arr, j++, tempK--);
        }
        i += 2 * k;
    }

    return String.valueOf(arr);
}

public static void swap (char[] arr, int j, int tempK) {
    char temp = arr[j];
    arr[j] = arr[tempK];
    arr[tempK] = temp;
}
