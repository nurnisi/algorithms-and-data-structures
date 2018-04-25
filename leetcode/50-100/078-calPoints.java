import java.util.*;

public class leetcode {

    public static void main(String[] args) {
        System.out.println(calPoints(new String[]{"5","-2","4","C","D","9","+","+"}));
    }

    public static int calPoints(String[] ops) {
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
