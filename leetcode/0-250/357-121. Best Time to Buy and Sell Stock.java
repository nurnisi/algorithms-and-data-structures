// 121. Best Time to Buy and Sell Stock
class Solution {
    public int maxProfit(int[] prices) {
        if (prices.length < 2)
            return 0;
        
        int min = prices[0], maxProf = 0;
        for (int i = 1; i < prices.length; i++) {
            maxProf = Math.max(maxProf, prices[i] - min);
            min = Math.min(min, prices[i]);
        }
        
        return maxProf;
    }
}