import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(letterCasePermutation("a12b"));
    }

    //solution by BFS
    public static List<String> letterCasePermutation(String S) {
        if (S == null) return new LinkedList<>();

        Queue<String> queue = new LinkedList<>();
        queue.add(S);
        for (int i = 0; i < S.length(); i++) {
            if (Character.isDigit(S.charAt(i))) continue;
            int size = queue.size();
            for (int j = 0; j < size; j++) {
                String cur = queue.poll();
                char[] arr = cur.toCharArray();

                arr[i] = Character.toUpperCase(arr[i]);
                queue.add(String.valueOf(arr));

                arr[i] = Character.toLowerCase(arr[i]);
                queue.add(String.valueOf(arr));
            }
        }

        return new LinkedList<>(queue);
    }

    //solution by loop
    public static List<String> letterCasePermutation3(String S) {
        List<String> list = new ArrayList<>(Arrays.asList(S));
        for (int i = 0; i < S.length(); i++) {
            for (int j = 0, size = list.size(); S.charAt(i) > '9' && j < size; j++) {
                char[] ch = list.get(j).toCharArray();
                ch[i] ^= 32;
                list.add(String.valueOf(ch));
            }
        }
        return list;
    }

    //my solution: recursive
    public static List<String> letterCasePermutation2(String S) {
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
