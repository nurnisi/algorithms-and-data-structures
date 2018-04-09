public static int maxProfit(int[] prices) {
    if(prices.length == 0) return 0;
    int res = 0;
    for (int i = 0; i < prices.length - 1; i++) {
        if(prices[i] < prices[i + 1]) {
            int max = prices[i];
            for (int j = i; j < prices.length; j++) {
                if(max < prices[j]) max = prices[j];
            }
            res = Math.max((max - prices[i]), res);
        }
    }
    return  res;
}

//Kadane's algorithm
public static int kadane(int[] prices) {
    int maxCurrent = prices[0], maxGlobal = prices[0];
    for (int i = 1; i < prices.length; i++) {
        maxCurrent = Math.max(prices[i], prices[i] + maxCurrent);
        if(maxGlobal < maxCurrent) maxGlobal = maxCurrent;
    }
    return maxGlobal;
}

//solution with Kadane's algorithm
public static int maxProfit(int[] prices) {
    if (prices.length == 0) return 0;
    int maxGlobal = 0, maxCurrent = 0;
    for (int i = 1; i < prices.length; i++) {
        maxCurrent = Math.max(0, maxCurrent + prices[i] - prices[i - 1]);
        if (maxGlobal < maxCurrent) maxGlobal = maxCurrent;
    }
    return maxGlobal;
}
