//sort
public static boolean checkPermutation(String str1, String str2) {
    if (str1.length() != str2.length()) return false;

    char[] arr1 = str1.toCharArray();
    Arrays.sort(arr1);
    str1 = new String(arr1);

    char[] arr2 = str2.toCharArray();
    Arrays.sort(arr2);
    str2 = new String(arr2);

    return str1.equals(str2);
}
