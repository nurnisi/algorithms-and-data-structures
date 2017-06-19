public static boolean isHappy(int n) {
    Map<Integer, Integer> map = new HashMap<>();
    return helper(n, map);
}

public static boolean helper(int n, Map<Integer, Integer> map) {
    if(map.get(n) != null) return false;
    map.put(n, 1);

    int sum = 0;
    while(n != 0) {
        sum += Math.pow(n % 10, 2);
        n /= 10;
    }
    if(sum == 1) return true;

    return helper(sum, map);
}

//without map/set
public static boolean isHappy(int n) {
    int slow = n, fast = n;
    do {
        slow = helper(slow);
        fast = helper(fast);
        fast = helper(fast);
    } while (slow == fast);
    if(slow == 1) return true;
    return false;
}

public static int helper(int n) {
    int sum = 0;
    while(n != 0) {
        sum += Math.pow(n % 10, 2);
        n /= 10;
    }
    return sum;
}
