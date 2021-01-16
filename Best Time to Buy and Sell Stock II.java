class Solution 
{
    public int maxProfit(int[] prices) 
    {
        int buyPrice = prices[0],
        int profit = 0;
        
        for(int i=1;i<prices.length;i++) 
        {
            if(prices[i] > buyPrice)
            {
                profit = profit + (prices[i] - buyPrice);
                buyPrice = prices[i];
            }
            else  buyPrice = prices[i];
        }
        
        return profit;
    }
}



Input: [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
             Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
             
Input: [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
             Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are
             engaging multiple transactions at the same time. You must sell before buying again.
