import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e3_3();
    }

    static void e3_3() {
        String s1 = sc.nextLine(), s2 = sc.nextLine();

        int len1 = s1.length(), len2 = s2.length();

        int[] n1 = new int[len1];
        for (int i = 0; i < len1; i++) n1[i] = s1.charAt(len1 - 1 - i) - '0';

        int[] n2 = new int[len2];
        for (int i = 0; i < len2; i++) n2[i] = s2.charAt(len2 - 1 - i) - '0';

        int[] n3 = new int[5001];
        int i3 = 0, carry;
        for (int i1 = 0; i1 < len1; i1++) {
            for (int i2 = 0; i2 < len2; i2++) {
                carry = n1[i1] * n2[i2];
                i3 = i1 + i2;
                while (carry > 0) {
                    carry += n3[i3];
                    n3[i3++] = carry % 10;
                    carry /= 10;
                }
            }
        }

        if (n3[i3] == 0) i3--;
        for (; i3 >= 0; i3--) System.out.print(n3[i3]);
    }

    static void e3_2() {
        String s1 = sc.nextLine(), s2 = sc.nextLine();

        int len1 = s1.length(), len2 = s2.length();

        int[] n1 = new int[len1];
        for (int i = 0; i < len1; i++) n1[i] = s1.charAt(len1 - 1 - i) - '0';

        int[] n2 = new int[len2];
        for (int i = 0; i < len2; i++) n2[i] = s2.charAt(len2 - 1 - i) - '0';

        int[] n3 = new int[5001];
        int i3 = 0, carry;
        for (int i1 = 0; i1 < len1; i1++) {
            i3 = i1;
            carry = 0;
            for (int i2 = 0; i2 < len2; i2++, i3++) {
                carry = carry + n3[i3] + n2[i2] * n1[i1];
                n3[i3] = carry % 10;
                carry /= 10;
            }
            n3[i3] = carry;
        }
        if (n3[i3] == 0) i3--;
        for (; i3 >= 0; i3--) System.out.print(n3[i3]);
    }

    static void e3() {
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();

        List<Integer> result = multiply(s1, s2.charAt(s2.length() - 1) - '0', 0);

        int len = s2.length();
        for (int i = len - 2; i >= 0; i--) {
            List<Integer> list = multiply(s1, s2.charAt(i) - '0', len - 1 - i);
            sum(result, list);
        }

        for (int i = result.size() - 1; i >= 0; i--) {
            System.out.print(result.get(i));
        }
    }

    static void sum(List<Integer> result, List<Integer> list) {
        int i = 0, c = 0;
        for (; i < result.size() && i < list.size(); i++) {
            int m = result.get(i) + list.get(i) + c;
            c = m / 10;
            result.set(i, m % 10);
        }

        while (i < list.size()) {
            int m = list.get(i) + c;
            c = m / 10;
            result.add(m % 10);
            i++;
        }

        if (c != 0) result.add(c);
    }

    static List<Integer> multiply(String s, int n, int zeros) {
        List<Integer> list = new ArrayList<>();
        for (int i = 0; i < zeros; i++) list.add(0);

        int c = 0, len = s.length();
        for (int i = len - 1; i >= 0; i--) {
            int m = (s.charAt(i) - '0') * n + c;
            c = m / 10;
            list.add(m % 10);
        }
        if (c > 0) list.add(c);

        return list;
    }
}