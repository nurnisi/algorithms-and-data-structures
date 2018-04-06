import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f4_2();
    }

    static void f4_2() {
        int n = Integer.valueOf(sc.nextLine());
        String s = sc.nextLine();
        Stack<Character> stack = new Stack<>();

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(' || ch == '{' || ch == '[') stack.push(ch);
            else if (stack.isEmpty()
                    || (ch == ')' && stack.peek() != '(')
                    || (ch == '}' && stack.peek() != '{')
                    || (ch == ']' && stack.peek() != '[')) {
                System.out.println("No");
                return;
            } else stack.pop();
        }

        if (stack.isEmpty()) System.out.println("Yes");
        else System.out.println("No");
    }

    static void f4() {
        int n = Integer.valueOf(sc.nextLine());
        String s = sc.nextLine();

        if (n % 2 == 1) {
            System.out.println("No");
            return;
        }

        char[] arr = new char[n];
        int cur = 0;

        for (int i = 0; i < s.length(); i++) {
            char ch = s.charAt(i);
            if (ch == '(' || ch == '{' || ch == '[') arr[cur++] = s.charAt(i);
            else {
                if ((cur - 1 < 0)
                        || (ch == ')' && arr[cur - 1] != '(')
                        || (ch == '}' && arr[cur - 1] != '{')
                        || (ch == ']' && arr[cur - 1] != '[')) {
                    System.out.println("No");
                    return;
                }
                cur--;
            }
        }

        if (cur == 0) System.out.println("Yes");
        else System.out.println("No");
    }
}