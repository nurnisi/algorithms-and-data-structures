public static String URLify(String str, int length) {
    char[] arr = str.toCharArray();
    for (int runner = arr.length - 1; runner >= 0; runner--) {
        if (arr[length - 1] == ' ') {
            arr[runner--] = '0';
            arr[runner--] = '2';
            arr[runner] = '%';
        } else arr[runner] = arr[length - 1];
        length--;
    }
    return new String(arr);
}
