import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        e5_2();
    }

    static int vLen = 0;

    static void e5_2() {
        int ii = sc.nextInt(), jj = sc.nextInt();
        String s = sc.next();
        int[] value = new int[6000];

        for (int i = 0; i < s.length(); i++) {
            int num = s.charAt(i) - '0';
            mul(value, ii);
            add(value, num < 10 ? num : num - 7);
        }

        int i = 0;
        int[] res = new int[6000];
        do {
            res[i++] = div(value, jj);
        } while(vLen > 0);

        for (int j = i - 1; j >= 0; j--) {
            System.out.print((char) (res[j] < 10 ? res[j] + '0' : res[j] + '7'));
        }
    }

    static int div(int[] value, int jj) {
        int rem = 0;
        boolean check = true;
        for (int i = vLen - 1; i >= 0; i--) {
            rem = rem * 10 + value[i];
            value[i] = rem / jj;
            if (value[i] == 0 && check) vLen--;
            else check = false;
            rem = rem % jj;
        }
        return rem;
    }

    static void mul(int[] value, int ii) {
        int c = 0;
        for (int i = 0; i < vLen; i++) {
            c = value[i] * ii + c;
            value[i] = c % 10;
            c /= 10;
        }
        while (c > 0) {
            value[vLen++] = c % 10;
            c /= 10;
        }
    }

    static void add(int[] value, int n) {
        int i = 0;
        while (n > 0) {
            n += value[i];
            value[i++] = n % 10;
            n /= 10;
        }
        vLen = Math.max(vLen, i);
    }

    //not suitable for long numbers
    static void e5_2_1() {
        int ii = sc.nextInt(), jj = sc.nextInt();
        String s = sc.next();
        int value = 0;

        for (int i = 0; i < s.length(); i++) {
            int num = s.charAt(i) - '0';
            value = value * ii + (num < 10 ? num : num - 7);
        }

        int numLen = 0;
        int[] res = new int[6000];
        do {
            res[numLen++] = value % jj;
            value /= jj;
        } while(value != 0);

        for (int i = numLen - 1; i >= 0; i--) System.out.print((char) (res[i] < 10 ? res[i] + '0' : res[i] + '7'));
    }

    //my solution: partial
    static void e5() {
        int I = sc.nextInt(), J = sc.nextInt();
        String n = sc.next();

        List<Integer> list = toDecimal(I,n);
        List<Character> list2 = fromDecimal(J, list);

        for (int i = list2.size() - 1; i >= 0; i--) System.out.print(list2.get(i));
    }

    static List<Character> fromDecimal(int J, List<Integer> list) {
        List<Character> res = new ArrayList<>();
        List<Integer> divide = new ArrayList<>();
        Collections.reverse(list);

        while (list.size() > 2) {
            int rem = divide(J, list, divide);
            res.add((char) (rem < 10 ? rem + '0' : rem + '0' + 7));

            list.clear();
            list.addAll(divide);
        }

        int num = 0;
        for (int i = 0; i < list.size(); i++) num = num * 10 + list.get(i);

        while (num >= J) {
            int rem = num % J;
            res.add((char) (rem < 10 ? rem + '0' : rem + '0' + 7));
            num /= J;
        }

        if (num != 0) res.add((char) (num < 10 ? num + '0' : num + '0' + 7));
        return res;
    }

    static int divide(int n, List<Integer> list, List<Integer> res) {
        res.clear();
        int i = 0, num = 0;

        while (num < n && i < list.size()) {
            num = num * 10 + list.get(i++);
            if (num >= n) {
                res.add(num / n);
                num %= n;
            } else if (!res.isEmpty()) res.add(0);
        }

        return num;
    }

    static List<Integer> toDecimal(int I, String n) {
        List<Integer> res = new ArrayList<>();
        int len = n.length();
        if (I == 10) for (int i = len - 1; i >= 0; i--) res.add(n.charAt(i) - '0');
        else {
            for (int i = 0; i < len; i++) {
                List<Integer> power = toPower(I, i);
                int cur = n.charAt(len - 1 - i) - '0';
                multiply(cur < 10 ? cur : cur - 7, power);
                sum(res, power);
            }
        }
        return res;
    }

    static void sum(List<Integer> res, List<Integer> power) {
        int c = 0, cur = 0;
        while (cur < res.size() && cur < power.size()) {
            c = res.get(cur) + power.get(cur) + c;
            res.set(cur++, c % 10);
            c /= 10;
        }

        while (cur < power.size()) {
            c = power.get(cur++) + c;
            res.add(c % 10);
            c /= 10;
        }

        if (c != 0) res.add(c);
    }

    static List<Integer> toPower(int n, int pow) {
        List<Integer> list = new ArrayList<>();
        if (pow == 0) list.add(1);
        else {
            list.add(n);
            for (int i = 1; i < pow; i++) {
                multiply(n, list);
            }
        }
        return list;
    }

    static void multiply(int n, List<Integer> list) {
        int c = 0;
        for (int j = 0; j < list.size(); j++) {
            c = list.get(j) * n + c;
            list.set(j, c % 10);
            c /= 10;
        }
        if (c != 0) list.add(c);
    }
}