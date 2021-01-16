class Solution 
{
    public int maxProfit(int[] prices) 
    {
        int profit = 0;
        int buyPrice = prices[0];
        
        // Each iteration we check to see if the current day is the day to buy.
        // If it is NOT the day to buy, we check to see if it is the day to sell to make the most profit. 
        for(int i=1;i<prices.length;i++)
        {
            // if statement is reponsible for finding the price to buy.
            if(prices[i] < buyPrice)    buyPrice = prices[i];
            
            // check if selling on the current day will yield a better profit margin.
             profit = Math.max(profit, prices[i] - buyPrice);
        }
        
        return profit;
    }
}

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
