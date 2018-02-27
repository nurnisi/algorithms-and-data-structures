import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        f1_2();
    }

    static void f1_2() {
        int[] A = new int[5];
        int[] B = new int[13];
        int[] C = new int[6];

        for (int i = 0; i < 5; i++) {
            A[i] = sc.nextInt();
            B[A[i] - 1]++;
        }

        for (int i = 0; i < 13; i++) {
            C[B[i]]++;
        }

        if (C[5] == 1) System.out.println("Impossible");
        else if (C[4] == 1) System.out.println("Four of a Kind");
        else if (C[3] == 1 && C[2] == 1) System.out.println("Full House");
        else if (C[3] == 1) System.out.println("Three of a Kind");
        else if (C[2] == 2) System.out.println("Two Pairs");
        else if (C[2] == 1) System.out.println("One Pair");
        else {
            int i = 0;
            while (B[i] != 1) i++;
            for (int j = 1; j < 5; j++) {
                if (B[i + j] != 1) {
                    System.out.println("Nothing");
                    return;
                }
            }
            System.out.println("Straight");
        }
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