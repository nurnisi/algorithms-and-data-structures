// 202. Happy Number
class Solution {
    public boolean isHappy(int n) {
        Set<Integer> set = new HashSet<>();
        set.add(n);
        while (true) {
            int sum = 0;
            while (n != 0) {
                int temp = n % 10;
                sum += temp * temp;
                n /= 10;
            }
            n = sum;
            if (n == 1) return true;
            if (set.contains(n)) return false;
            set.add(n);
        }
    }
}

class Solution {
    int sqSum(int n) {
        int sum = 0, tmp;
        while (n != 0) {
            tmp = n % 10;
            sum += tmp * tmp;
            n /= 10;
        }
        return sum;
    }
    
    public boolean isHappy(int n) {
        int slow = n, fast = n;
        do {
            slow = sqSum(slow);
            fast = sqSum(fast);
            fast = sqSum(fast);
        } while (slow != fast);
        if (slow == 1) return true;
        return false;
    }
}