import java.util.*;

public class leetcode {

    public static void main(String[] args) {

    }

    public char nextGreatestLetter(char[] letters, char target) {
        if (letters[letters.length - 1] <= target) return letters[0];
        for (char ch : letters)
            if (target < ch) {
                target = ch;
                break;
            }
        return target;
    }
}