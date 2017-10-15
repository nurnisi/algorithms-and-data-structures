    static void a() {
        int n = sc.nextInt();
        int m = sc.nextInt();

        int minN = Integer.MAX_VALUE;
        boolean[] arr1 = new boolean[10];
        for (int i = 0; i < n; i++) {
            int int1 = sc.nextInt();
            arr1[int1] = true;
            minN = Math.min(minN, int1);
        }

        int minM = Integer.MAX_VALUE;
        boolean[] arr2 = new boolean[10];
        for (int i = 0; i < m; i++) {
            int int2 = sc.nextInt();
            arr2[int2] = true;
            minM = Math.min(minM, int2);
        }

        for (int i = 1; i < 10; i++) {
            if (arr1[i] && arr2[i]) {
                System.out.println(i);
                return;
            }
        }

        if (minM > minN) System.out.println(minN + "" + minM);
        else System.out.println(minM + "" + minN);
    }

    static void b() {
        int n = sc.nextInt();
        int k = sc.nextInt();

        long max = Integer.MIN_VALUE;
        long min = Integer.MAX_VALUE;
        for (int i = 0; i < n; i++) {
            int curr = sc.nextInt();
            max = Math.max(max, curr);
            min = Math.min(min, curr);
        }

        if (k == 1) System.out.println(min);
        else System.out.println(max);
    }

    