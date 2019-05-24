import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        c3();
    }

    static void c3_2() {
        int empty = sc.nextInt();
        int full = sc.nextInt();
        int n = sc.nextInt();

        Map<Integer, Integer> W = new HashMap<>();
        for (int i = 0; i < n; i++) {
            W.put(sc.nextInt(), sc.nextInt());
        }

        long[] min = new long[full - empty + 1];
        Arrays.fill(min, -1);
        min[0] = 0;

        long[] max = new long[full - empty + 1];
        Arrays.fill(max, -1);
        max[0] = 0;


        for (int kind : W.keySet()) {
            int wOfKind = W.get(kind);
            for (int weight = 1; weight < min.length; weight++) {
                if (wOfKind <= weight) {
                    if (min[weight - wOfKind] >= 0) {
                        if (min[weight] == -1) min[weight] = min[weight - wOfKind] + kind;
                        else min[weight] = Math.min(min[weight], min[weight - wOfKind] + kind);
                    }
                    if (max[weight - wOfKind] >= 0) {
                        if (max[weight] == -1) max[weight] = max[weight - wOfKind] + kind;
                        else max[weight] = Math.max(max[weight], max[weight - wOfKind] + kind);
                    }
                }
            }
        }

        if (min[min.length - 1] == -1 || max[max.length - 1] == -1) System.out.println("This is impossible.");
        else System.out.println(min[min.length - 1] + " " + max[max.length - 1]);
    }

    static void c3() {
        int empty = sc.nextInt();
        int full = sc.nextInt();
        int n = sc.nextInt();

        Map<Integer, Integer> W = new HashMap<>();
        for (int i = 0; i < n; i++) {
            W.put(sc.nextInt(), sc.nextInt());
        }

        long[] min = new long[full - empty + 1];
        long[] max = new long[full - empty + 1];
        min[0] = 0;
        max[0] = 0;
        for (int weight = 1; weight < min.length; weight++) {
            boolean checkMin = true;
            boolean checkMax = true;
            for (int kind : W.keySet()) {
                int wOfKind = W.get(kind);
                if (wOfKind <= weight) {
                    if (min[weight - wOfKind] >= 0) {
                        if (checkMin) min[weight] = min[weight - wOfKind] + kind;
                        else min[weight] = Math.min(min[weight], min[weight - wOfKind] + kind);
                        checkMin = false;
                    }
                    if (max[weight - wOfKind] >= 0) {
                        if (checkMax) max[weight] = max[weight - wOfKind] + kind;
                        else max[weight] = Math.max(max[weight], max[weight - wOfKind] + kind);
                        checkMax = false;
                    }
                }
            }
            if (checkMin) min[weight] = -1;
            if (checkMax) max[weight] = -1;
        }
        if (min[min.length - 1] == -1 || max[max.length - 1] == -1) System.out.println("This is impossible.");
        else System.out.println(min[min.length - 1] + " " + max[max.length - 1]);
    }
}