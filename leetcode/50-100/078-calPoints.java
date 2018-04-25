import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(calPoints(new String[]{"5","-2","4","C","D","9","+","+"}));
    }

    public static int calPoints(String[] ops) {
        Stack<Integer> stack = new Stack<>();

        for (String s : ops) {
            if (s.equals("C")) stack.pop();
            else if (s.equals("D")) stack.add(stack.peek() * 2);
            else if (s.equals("+")) {
                int top = stack.pop(), newTop = stack.peek() + top;
                stack.add(top);
                stack.add(newTop);
            } else stack.add(Integer.valueOf(s));
        }

        int ans = 0;
        for (int i : stack) ans += i;
        return ans;
    }

    public static int calPoints2(String[] ops) {
        Stack<Integer> stack = new Stack<>();
        int sum = 0;
        for (String s : ops) {
            char ch = s.charAt(0);
            if (ch == 'C' && !stack.isEmpty()) {
                sum -= stack.pop();
            } else if (ch == 'D' && !stack.isEmpty()) {
                int n = stack.peek();
                sum += n * 2;
                stack.add(n * 2);
            } else if (ch == '+' && stack.size() >= 2) {
                int first = stack.pop(), second = stack.peek();
                sum += first + second;
                stack.add(first);
                stack.add(first + second);
            } else {
                int n = Integer.valueOf(s);
                sum += n;
                stack.add(n);
            }
        }
        return sum;
    }
}
