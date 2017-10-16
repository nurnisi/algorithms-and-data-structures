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