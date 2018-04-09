public int maxProfit(int[] prices) {
    if(prices.length == 0) return 0;
    int res = 0, runner = prices[0];
    for (int i = 1; i < prices.length; i++) {
        if(prices[i] < prices[i - 1]) {
            res += prices[i - 1] - runner;
            runner = prices[i];
        }
    }
    if(prices[prices.length - 1] > runner) res += prices[prices.length - 1] - runner;
    return res;
}
