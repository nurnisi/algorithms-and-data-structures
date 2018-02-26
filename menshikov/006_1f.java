import java.lang.reflect.Array;
import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f1();
    }

    static void f1() {
        Map<Integer, Integer> map = new HashMap<>();
        int[] arr = new int[5];
        for (int i = 0; i < 5; i++) {
            int k = sc.nextInt();
            map.put(k, map.getOrDefault(k, 0) + 1);
            arr[i] = k;
        }

        if (map.size() == 1) System.out.println("Impossible");
        else if (map.size() == 2) {
            if (map.values().contains(4)) System.out.println("Four of a Kind");
            else System.out.println("Full House");
        } else if (map.size() == 3) {
            if (map.values().contains(3)) System.out.println("Three of a Kind");
            else System.out.println("Two Pairs");
        } else if (map.size() == 4) System.out.println("One Pair");
        else {
            Arrays.sort(arr);
            for (int i = 0; i < 4; i++) {
                if (arr[i] + 1 != arr[i + 1]) {
                    System.out.println("Nothing");
                    return;
                }
            }
            System.out.println("Straight");
        }
    }
}