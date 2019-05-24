public String reverseString(String s) {
    int i = 0;
    int j = s.length() - 1;
    char[] arr = s.toCharArray();
    while(i < j) {
        char ch = arr[i];
        arr[i++] = arr[j];
        arr[j--] = ch;
    }
    return new String(arr);
}
