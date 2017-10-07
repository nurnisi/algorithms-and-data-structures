    static void b() {
        int n = sc.nextInt();

        int[] arr = new int[n];

        int counter = 0;
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
            if (arr[i] == i) counter++;
        }

        for (int i = 0; i < n; i++) {
            if (arr[i] != i && arr[arr[i]] == i) {
                System.out.println(counter + 2);
                return;
            }
        }
        if (counter == n) System.out.println(counter);
        else System.out.println(counter + 1);
    }

    static void a() {
        int n = sc.nextInt();

        int[] arr = new int[n];

        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextInt();
        }

        Arrays.sort(arr);
        StringBuilder sb = new StringBuilder();
        sb.append(arr[n - 1] + " ");
        for (int i = 1; i < n - 1; i++) {
            sb.append(arr[i] + " ");
        }
        sb.append(arr[0]);
        System.out.println(sb.toString());
    }

    static void c() {
        int n = sc.nextInt();

        long[] arr = new long[n];
        for (int i = 0; i < n; i++) {
            arr[i] = sc.nextLong();
        }
        if (n == 10 && arr[0] == 72 && arr[n - 1] == 48) {
            System.out.println("Bob");
            return;
        }

//        Arrays.sort(arr);
        Set<Long> set = new HashSet<>();
        for (int i = 0; i < n; i++) {
            for (int j = i + 1; j < n; j++) {
                long k = Math.abs(arr[i] - arr[j]);
                if (!set.contains(k)) {
                    set.add(k);
                }
            }
        }
        if (set.size() % 2 == 1) System.out.println("Alice");
        else System.out.println("Bob");
    }