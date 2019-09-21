// 7. Reverse Integer
class Solution {
    public int reverse2(int x) {
        long res = 0;
        boolean neg = x >= 0 ? false : true;
        x = Math.abs(x);
        while (x != 0) {
            res = res * 10 + x % 10;
            x /= 10;
        }
        
        if (neg)
            res *= -1;
        
        if (res < Math.pow(-2, 31) || res >= Math.pow(2, 31))
            return 0;
        
        return (int)res;
    }

    public int reverse(int x) {
        int res = 0, prev = 0;
        while (x != 0) {
            res = res * 10 + x % 10;
            if ((res - x % 10) / 10 != prev)
                return 0;
            prev = res;
            x /= 10;
        }
        return res;
    }
}