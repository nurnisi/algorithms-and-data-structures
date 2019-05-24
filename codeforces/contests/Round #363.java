    static void a() {
        int n = Integer.parseInt(sc.nextLine());
        String str = sc.nextLine();

        int[] arr = new int[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int min = Integer.MAX_VALUE;
        for (int i = 1; i < n; i++) {
            if (str.charAt(i - 1) == 'R' && str.charAt(i) == 'L') {
                min = Math.min(min, (arr[i] - arr[i - 1]) / 2);
            }
        }

        System.out.println(min != Integer.MAX_VALUE ? min : -1);
    }
    
    static void b() {
        int n = sc.nextInt();
        int m = sc.nextInt();
        sc.nextLine();

        String[] arr = new String[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLine();
        }

        int k = - 1, l = -1, constL = -1;
        for (int i = 0; i < n; i++) {
            String str = arr[i];
            int c = 0;
            for (int j = 0; j < m; j++) {
                if (str.charAt(j) == '*') {
                    c++;
                    l = j;
                }
            }

            if (c > 1) {
                if (k == -1) k = i;
                else {
                    System.out.println("NO");
                    return;
                }
            } else if (c == 1) {
                if (constL == -1) constL = l;
                else if (constL != l) {
                    System.out.println("NO");
                    return;
                }
            }
        }

        System.out.println("YES");
        System.out.println((k == -1 ? 1 : ++k) + " " + (constL == -1 ? 1 : ++constL));

    }

    static void c() {
        int n = sc.nextInt();
        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        int cg = 0;
        if (arr[0] != 0) cg++;
        for (int i = 1; i < n; i++) {
            if (arr[i] != 0) {
                if (arr[i] == 1) {
                    if (arr[i - 1] != 1) {
                        cg++;
                    } else arr[i] = 0;
                }
                else if (arr[i] == 2) {
                    if (arr[i - 1] != 2) {
                        cg++;
                    } else arr[i] = 0;
                }
                else if (arr[i] == 3) {
                    if (arr[i - 1] == 1) {
                        arr[i] = 2;

                    } else if (arr[i - 1] == 2) {
                        arr[i] = 1;
                    }
                    cg++;
                }
            }
        }

        System.out.println(n - cg);
    }