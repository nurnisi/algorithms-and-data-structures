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

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        if (k >= 3) {
            int max = arr[0];
            for (int i = 1; i < n; i++) {
                max = Math.max(max, arr[i]);
            }
            System.out.println(max);
            return;
        } else if (k == 2) {
            int[] pref = new int[n];
            int[] suf = new int[n];

            pref[0] = arr[0];
            for (int i = 1; i < n; i++) {
                pref[i] = Math.min(pref[i - 1], arr[i]);
            }

            suf[n - 1] = arr[n - 1];
            for (int i = n - 2; i >= 0; --i) {
                suf[i] = Math.min(arr[i], suf[i + 1]);
            }
            int ans = Integer.MIN_VALUE;
            for (int i = 0; i < n - 1; i++) {
                int max = Math.max(pref[i], suf[i + 1]);
                ans = Math.max(ans, max);
            }
            System.out.println(ans);
            return;
        } else if (k == 1) {
            int min = arr[0];
            for (int i = 1; i < n; i++) {
                min = Math.min(min, arr[i]);
            }
            System.out.println(min);
            return;
        }
    }

    static void c() {
        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) arr[i] = sc.nextInt();

        for (int i = 0; i < n; i++) {
            int m = arr[i];
            if (m < 4 || m == 5 || m == 7 || m == 11) System.out.println(-1);
            else {
                if (m % 4 == 0) System.out.println(m / 4);
                else if (m % 4 == 1) System.out.println(1 + (m - 9) / 4);
                else if (m % 4 == 2) System.out.println(1 + (m - 6) / 4);
                else if (m % 4 == 3) System.out.println(2 + (m - 15) / 4);
            }
        }
    }

    