import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a4();
    }

    static void a4() {
        int M = sc.nextInt(), N = sc.nextInt();

        boolean check = true;
        for (; M <= N; M++) {
            List<Integer> list = new ArrayList<>();
            for (int i = 2; i * 2 <= M; i++)
                if (M % i == 0)
                    list.add(i);

            if (list.size() != 0) {
                int res = 1;
                for (int i : list) res += i;
                if (res == M) {
                    System.out.println(M);
                    check = false;
                }
            }
        }

        if (check) System.out.print("Absent");
    }
}