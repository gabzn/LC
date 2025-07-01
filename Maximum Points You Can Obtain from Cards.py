https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/

class Solution:
    def maxScore(self, cards: List[int], k: int) -> int:
        N = len(cards)
        WINDOW_SIZE = N - k
        TOTAL = sum(cards)

        # If we have to take all N cards, just return the sum
        if N == k:
            return TOTAL

        # Instead of getting the window max, we get the window min
        # We then use total to subtract window min to get window max        
        window_sum = 0
        window_min_sum = inf

        for i, point in enumerate(cards):
            # Add to window
            window_sum += point

            # Check window size
            if i + 1 - WINDOW_SIZE < 0:
                continue
            
            # Update min
            window_min_sum = min(window_min_sum, window_sum)

            # Remove leftmost item from window
            window_sum -= cards[i + 1 - WINDOW_SIZE]

        return TOTAL - window_min_sum
---------------------------------------------------------------------------
class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        LEN, max_score = len(cardPoints), 0                
        prefix_sum = self.get_prefix_sum(cardPoints, LEN)
        
        # Maintain a window of size LEN - K and use it to loop through the prefix sum
        # This works because when we maintain a window of size LEN - K, there's always only K elements left in the list.
        window_size = LEN - k
        window_r_index = window_size - 1
        
        while window_r_index < LEN:
            current_window_sum = 0
            window_l_index = window_r_index - window_size + 1
            
            # the current score = total_pts - current_window_sum
            if window_l_index == 0:
                current_window_sum = prefix_sum[window_r_index]
            else:
                current_window_sum = prefix_sum[window_r_index] - prefix_sum[window_l_index-1]
            
            max_score = max(max_score, prefix_sum[-1] - current_window_sum)
            window_r_index += 1
    
        return max_score
    
    def get_prefix_sum(self, nums, length):
        prefix_sum = [nums[0]]
        
        for index in range(1, length):
            prefix_sum.append(prefix_sum[-1] + nums[index])
        
        return prefix_sum
