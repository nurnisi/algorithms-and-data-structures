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