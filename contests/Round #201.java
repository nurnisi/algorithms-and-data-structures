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

        int prev = sc.nextInt();
        int max = prev;
        int gcd = prev;
        for (int i = 1; i < n; i++) {
            int curr = sc.nextInt();
            gcd = gcd(gcd, curr);
            prev = curr;
            if (curr > max) max = curr;
        }

        int moves = max / gcd - n;
        if (moves % 2 == 1) System.out.println("Alice");
        else System.out.println("Bob");
    }

    static int gcd(int a, int b) {
        if (b == 0) return a;
        return gcd(b, a % b);
    }

    static void d() {
        String s1 = sc.nextLine();
        String s2 = sc.nextLine();
        String virus = sc.nextLine();

        Map<Character, List<Integer>> map = new HashMap<>();
        for (int i = 0; i < s1.length(); i++) {
            char ch = s1.charAt(i);
            List<Integer> list = map.getOrDefault(ch, new ArrayList<>());
            list.add(i);
            map.put(ch, list);
        }

        String res = "";
        for (int i = 0; i < s2.length(); i++) {
            List<Integer> list = map.getOrDefault(s2.charAt(i), new ArrayList<>());
            for (int j = 0; j < list.size(); j++) {
                StringBuilder sb = new StringBuilder();
                sb.append(s2.charAt(i));
                int k = list.get(j);
                for (int l = i + 1; l < s2.length(); l++) {
                    List<Integer> list2 = map.getOrDefault(s2.charAt(l), new ArrayList<>());
                    for (int m : list2) {
                        if (k < m) {
                            sb.append(s2.charAt(l));
                            k = m;
                        }
                    }
                }
                String temp = sb.toString();
                if (!temp.contains(virus) && temp.length() > res.length()) res = temp;
            }
        }

        if (res.length() == 0) System.out.println(0);
        else System.out.println(res);
    }