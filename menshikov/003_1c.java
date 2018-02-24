import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c1();
    }

    static void c1modified() {
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int[] cons = new int[n];
        int maxIndex = 0, max = 0;
        for (int i = n - 1; i >= 0; i--) {
            int k = 0;
            for (int j = i + 1; j < n; j++) {
                if (arr[i] < arr[j]) k = Math.max(k, cons[j]);
            }
            cons[i] = k + 1;
            if (max < cons[i]) {
                max = cons[i];
                maxIndex = i;
            }
        }

        System.out.println(max);
        System.out.print(arr[maxIndex] + " ");
        for (int i = maxIndex + 1; i < n && cons[maxIndex] > 0; i++) {
            if (cons[maxIndex] - 1 == cons[i]) {
                System.out.print(arr[i] + " ");
                maxIndex = i;
            }
        }
    }

    static void c1() {
        int n = sc.nextInt();
        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int[] cons = new int[n];
        int maxIndex = 0, max = 0;
        for (int i = 0; i < n; i++) {
            int k = 0;
            for (int j = i - 1; j >= 0; j--) {
                if (arr[i] > arr[j]) k = Math.max(k, cons[j]);
            }
            cons[i] = k + 1;
            if (max < cons[i]) {
                max = cons[i];
                maxIndex = i;
            }
        }

        Stack<Integer> stack = new Stack<>();
        stack.push(arr[maxIndex]);
        for (int i = maxIndex - 1; i >= 0; i--) {
            if (cons[i] == cons[maxIndex] - 1) {
                stack.push(arr[i]);
                maxIndex = i;
            }
        }

        System.out.println(max);
        while (!stack.isEmpty()) System.out.println(stack.pop());
    }
}