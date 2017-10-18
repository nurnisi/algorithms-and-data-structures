    static void a() {
        int n = sc.nextInt();
        int a = sc.nextInt();
        int b = sc.nextInt();
        int c = sc.nextInt();

        n--;

        if (n == 0) System.out.println(0);
        else if (n == 1) System.out.println(Math.min(a, b));
        else {
            int min = Math.min(a, Math.min(b, c));

            if (min == c) {
                System.out.println(Math.min(a, b) + (c * (n - 1)));
            } else {
                System.out.println(min * n);
            }
        }
    }

    static void b() {
        int n = sc.nextInt();
        int k = sc.nextInt();
        int m = sc.nextInt();

        Map<Integer, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < n; i++) {
            int cur = sc.nextInt();
            List<Integer> list = map.getOrDefault(cur % m, new ArrayList<>());
            list.add(cur);
            map.put(cur % m, list);
            if (list.size() == k) {
                System.out.println("Yes");
                for (int j : list) System.out.print(j + " ");
                return;
            }
        }

        System.out.println("No");
    }

    static void c() {
        int n = sc.nextInt();

        if (n < 10) System.out.println(0);
        else {
            int m = n;
            List<Integer> list = new ArrayList<>();
            while (n / m < 2) {
                int k = m;
                int sum = 0;
                while (k > 0) {
                    sum += k % 10;
                    k /= 10;
                }

                if (sum + m == n) list.add(m);
                m--;
            }

            System.out.println(list.size());
            if (list.size() > 0) {
                for (int i : list) System.out.println(i);
            }
        }
    }