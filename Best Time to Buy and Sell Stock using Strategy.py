https://leetcode.com/problems/best-time-to-buy-and-sell-stock-using-strategy/

class Solution:
    def maxProfit(self, prices: List[int], strategy: List[int], k: int) -> int:
        total_profit = window_sum = 0
        
        # First half of the window
        # If we don't make any changes, the profit is p * s
        # If we perform the modification, we'll go from p * s to p * 0
        # p * s -> p * 0, the delta is (p * 0) - (p * s)
        for p, s in zip(prices[:k // 2], strategy[:k // 2]):
            total_profit += (p * s)
            window_sum += (p * 0) - (p * s)

        # Second half of the window
        # If we don't make any changes, the profit is p * s
        # If we perform the modification, we'll go from p * s to p * 1
        # p * s -> p * 1, the delta is (p * 1) - (p * s)
        for p, s in zip(prices[k // 2: k], strategy[k // 2: k]):
            total_profit += (p * s)
            window_sum += (p * 1) - (p * s)
        
        max_window_sum = max(window_sum, 0)

        """
        [0, 1, 2, 3]
           [1, 2, 3, 4]
        
        When we slide the window to the right, 3 things happen:
        Index 0 needs to be removed from the window: - ((p * 0) - (p * s))
        Index 4 needs to be added to the window: + (p * 1) - (p * s)
        Index 2 needs to be moved to the left half: 
            ((p * 1) - (p * s)) - ((p * 0) - (p * s))
            p - p s + p s
            p
        """
        for i in range(k, len(prices)):
            p, s = prices[i], strategy[i]
            total_profit += (p * s)

            leftmost_index = i - k
            remove = (prices[leftmost_index] * 0) - (prices[leftmost_index] * strategy[leftmost_index])

            into_window = (p * 1) - (p * s)

            middle_index = i - (k // 2)
            move_over = prices[middle_index]

            window_sum += - remove + into_window - move_over
            max_window_sum = max(max_window_sum, window_sum)

        return total_profit + max_window_sum
