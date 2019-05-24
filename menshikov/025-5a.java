import java.util.*;

public class main {

    static Scanner sc = new Scanner(System.in);

    public static void main(String[] args) {
        a5();
    }

    static void a5() {
        int M = sc.nextInt(), N = sc.nextInt();
        boolean check = true;
        for (int i = 0; i < friendly.length; i++) {
            if (M <= friendly[i][0] && friendly[i][1] <= N) {
                check = false;
                System.out.println(friendly[i][0] + " " + friendly[i][1]);
            }
        }

        if (check) System.out.println("Absent");
    }

    static int[][] friendly = {
            {220, 284},
            {1184, 1210},
            {2620, 2924},
            {5020, 5564},
            {6232, 6368},
            {10744, 10856},
            {12285, 14595},
            {17296, 18416},
            {63020, 76084},
            {66928, 66992},
            {67095, 71145},
            {69615, 87633},
            {79750, 88730},
            {100485, 124155},
            {122265, 139815},
            {122368, 123152},
            {141664, 153176},
            {142310, 168730},
            {171856, 176336},
            {176272, 180848},
            {185368, 203432},
            {196724, 202444},
            {280540, 365084},
            {308620, 389924},
            {319550, 430402},
            {356408, 399592},
            {437456, 455344},
            {469028, 486178},
            {503056, 514736},
            {522405, 525915},
            {600392, 669688},
            {609928, 686072},
            {624184, 691256},
            {635624, 712216},
            {643336, 652664},
            {667964, 783556},
            {726104, 796696},
            {802725, 863835},
            {879712, 901424},
            {898216, 980984}
    };

    static void getFriendlyNumbers() {
        int M = 1, N = 1000000;
        int[] arr = new int[1000001];

        for (int i = M; i <= N; i++) {
            for (int j = 2; j <= i / 2; j++) {
                if (i % j == 0) arr[i] += j;
                //if (j * j > i && arr[i] == 0) break;
            }
            arr[i] += 1;
        }

        boolean check = true;
        for (; M < N; M++)
            if (arr[M] >= M && arr[arr[M]] == M) {
                check = false;
                System.out.println("{" + M + ", " + arr[M] + "},");
            }

        if (check) System.out.println("Absent");
    }
}