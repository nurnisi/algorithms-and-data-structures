public static boolean isAnagram(String s, String t) {
    int[] arr = new int[26];
    for (char i : s.toCharArray()) arr[i - 'a']++;
    for (char i : t.toCharArray()) arr[i - 'a']--;
    for (int i : arr)
        if (i != 0) return false;
    return true;
}
