import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(selfDividingNumbers(1, 22));
    }

    public static List<Integer> selfDividingNumbers(int left, int right) {
        List<Integer> list = new ArrayList<>();
        while (left <= right) {
            if (selfDivisible(left)) list.add(left);
            left++;
        }
        return list;
    }

    public static boolean selfDivisible(int num) {
        int temp = num, ones;
        while (temp != 0) {
            ones = temp % 10;
            if (ones == 0 || num % ones != 0) return false;
            temp /= 10;
        }
        return true;
    }
}
