package miscellaneous;
import java.lang.*;

/*
    Knuth–Morris–Pratt (KMP) 
    Pattern Matching (Substring search)
*/
class KMP {
    public static boolean KMP(String A, String B) {
        char[] text = A.toCharArray();
        char[] pattern = B.toCharArray();

        int[] temp = computeTemporaryArray(pattern);
        int i = 0, j = 0;
        while (i < text.length && j < pattern.length) {
            if (text[i] == pattern[j]) {
                i++;
                j++;
            } else {
                if (j != 0) j = temp[j - 1];
                else i++;
            }
        }
        if (j == pattern.length) return true;
        return false;
    }

    public static int[] computeTemporaryArray(char[] pattern) {
        int[] temp = new int[pattern.length];
        int index = 0;
        for (int i = 1; i < pattern.length;) {
            if (pattern[i] == pattern[index])
                temp[i++] = ++index;
            else {
                if (index != 0)
                    index = temp[index - 1];
                else
                    temp[i++] = 0;
            }
        }
        return temp;
    }
}