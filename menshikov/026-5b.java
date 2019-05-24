import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        b5_2();
    }

    static void b5_2() {
        int N = sc.nextInt();
        char[] brackets = {'(', ')', '[', ']'};
        char[] arr = new char[N];
        Stack<Character> s = new Stack<>();

        rec(0, N, arr, brackets, s);
    }

    static void rec(int cur, int N, char[] arr, char[] brackets, Stack<Character> s) {
        if (cur == N) {
            if (s.isEmpty()) System.out.println(String.valueOf(arr));
        } else {
            for (char ch : brackets) {
                arr[cur] = ch;
                if ((ch == '(' || ch == '[') && s.size() <= N / 2) {
                    s.add(ch);
                    rec(cur + 1, N, arr, brackets, s);
                    s.pop();
                } else if (s.isEmpty()
                        || (s.peek() == '(' && ch != ')')
                        || (s.peek() == '[' && ch != ']')) {
                    continue;
                } else {
                    char prev = s.pop();
                    rec(cur + 1, N, arr, brackets, s);
                    s.add(prev);
                }
            }
        }
    }

    //time limit exceeded
    static void b5() {
        int N = sc.nextInt();
        char[] brackets = {'(', ')', '[', ']'};
        char[] arr = new char[N];

        rec1(0, N, arr, brackets);
    }

    static void rec1(int cur, int N, char[] arr, char[] brackets) {
        if (cur == N) {
            Stack<Character> s = new Stack<>();
            for (char ch : arr) {
                if (ch == '(' || ch == '[') s.add(ch);
                else if (s.isEmpty()
                        || (s.peek() == '(' && ch != ')')
                        || (s.peek() == '[' && ch != ']')) return;
                else s.pop();
            }
            if (s.isEmpty()) System.out.println(String.valueOf(arr));
        } else {
            for (char ch : brackets) {
                arr[cur] = ch;
                rec1(cur + 1, N, arr, brackets);
            }
        }
    }
}