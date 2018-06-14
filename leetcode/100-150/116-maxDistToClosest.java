    public static int maxDistToClosest(int[] seats) {
        int left = 0, right = 0;
        while (seats[left] != 1) left++;
        while (seats[seats.length - right - 1] != 1) right++;
        int res = Math.max(left, right);

        int[] arr = new int[seats.length];
        for (int i = 0, count = 0; i < seats.length; i++, count++) {
            if (seats[i] == 1) {
                res = Math.max(res, count /2);
                count = 0;
            }
            arr[i] = count;
        }

        return res;
    }

    public static int maxDistToClosest(int[] seats) {
        int N = seats.length;
        int[] left = new int[N], right = new int[N];
        Arrays.fill(left, N);
        Arrays.fill(right, N);
        
        for (int i = 0; i < N; i++) {
            if (seats[i] == 1) left[i] = 0;
            else if (i > 0) left[i] = left[i - 1] + 1;
        }
        
        for (int i = N - 1; i >=0; i--) {
            if (seats[i] == 1) right[i] = 0;
            else if (i < N - 1) right[i] = right[i + 1] + 1;
        }
        
        int ans = 0;
        for (int i = 0; i < N; i++)
            if (seats[i] == 0)
                ans = Math.max(ans, Math.min(left[i], right[i]));
        return ans;
    }