import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(numberOfLines(new int[]{4,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10,10}, "bbbcccdddaaa"));
    }

    public static int[] numberOfLines(int[] widths, String S) {
        int lines = 1, curWidth = 0;
        for (char ch : S.toCharArray()) {
            int w = widths[ch - 'a'];
            if (curWidth + w > 100) {
                curWidth = w;
                lines++;
            } else curWidth += w;
        }
        return new int[]{lines, curWidth};
    }
}
