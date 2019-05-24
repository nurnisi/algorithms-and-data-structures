import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        friends();
    }

    static void friends() {
        int[] arr = new int[3];
        arr[0] = sc.nextInt();
        arr[1] = sc.nextInt();
        arr[2] = sc.nextInt();

        Arrays.sort(arr);

        System.out.println(arr[2] - arr[0]);
    }
}