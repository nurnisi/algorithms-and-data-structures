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