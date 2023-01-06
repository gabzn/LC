https://leetcode.com/problems/jump-game-vi/
  
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        N = len(nums)
        scores = [0] * N
        scores[0] = nums[0]
        
        deque = collections.deque()
        deque.append((nums[0], 0))
        
        for index in range(1, N):
            
            # Make sure the window size is still valid
            while deque and index - deque[0][1] > k:
                deque.popleft()
        
            score = nums[index] + deque[0][0]
            
            # Update the values in the deque to make sure values are monotonically decreasing
            while deque and score > deque[-1][0]:
                deque.pop()
            
            scores[index] = score
            deque.append((score, index))
        
        return scores[-1]
