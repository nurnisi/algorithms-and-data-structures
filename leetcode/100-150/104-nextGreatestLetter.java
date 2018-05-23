import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    public char nextGreatestLetter(char[] letters, char target) {
        for (char ch : letters)
            if (ch > target)
                return ch;
        return letters[0];
    }

    public char nextGreatestLetter3(char[] letters, char target) {
        boolean[] seen = new boolean[26];
        for (char ch : letters)
            seen[ch - 'a'] = true;

        while (true) {
            target++;
            if (target > 'z') target = 'a';
            if (seen[target - 'a']) return target;
        }
    }

    public char nextGreatestLetter2(char[] letters, char target) {
        if (letters[letters.length - 1] <= target) return letters[0];
        for (char ch : letters)
            if (target < ch) {
                target = ch;
                break;
            }
        return target;
    }
}