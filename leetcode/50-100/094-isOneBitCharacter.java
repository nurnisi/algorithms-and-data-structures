import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(isOneBitCharacter(new int[]{1,1,0}));
    }

    public static boolean isOneBitCharacter(int[] bits) {
        int i = 0;
        while (i < bits.length - 1)
            i += bits[i] + 1;
        return i == bits.length - 1;
    }

    public static boolean isOneBitCharacter2(int[] bits) {
        int i = 0, len = bits.length;
        while (i <= len - 2) {
            if (bits[i] == 1) i += 2;
            else i++;
        }
        if (len - i == 1 || (bits[len - 1] == 0 && bits[len - 2] == 0)) return true;
        return false;
    }
}