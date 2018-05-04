import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(letterCasePermutation("12345a"));
    }

    public static List<String> letterCasePermutation(String S) {
        char[] arr = S.toLowerCase().toCharArray();
        List<String> list = new ArrayList<>();

        recur(0, list, arr);

        return list;
    }

    public static void recur(int cur, List<String> list, char[] arr) {
        list.add(String.valueOf(arr));
        for (;cur < arr.length; cur++) {
            int n = arr[cur] - 'a';
            if (n >= 0 && n < 26) {
                arr[cur] = Character.toUpperCase(arr[cur]);
                recur(cur + 1, list, arr);
                arr[cur] = Character.toLowerCase(arr[cur]);
            }
        }
    }

}
