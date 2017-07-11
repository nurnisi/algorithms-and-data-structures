public static boolean palindromePermutation(String str) {
    int[] arr = new int[26];
    str = str.toLowerCase();
    for (char ch : str.toCharArray())
        if (ch != ' ')
            arr[ch - 'a']++;

    boolean check = false;
    for (int i : arr)
        if (i % 2 != 0) {
            if (!check) check = !check;
            else return false;
        }

    return true;
}

//with int
public static  boolean palindromePermutationWithInt(String str) {
    int i = 0;
    str = str.toLowerCase();
    for (char ch : str.toCharArray())
        if (ch != ' ')
            i ^= (1 << (ch - 'a'));

    return i == 0 || (i & (i - 1)) == 0;
}
