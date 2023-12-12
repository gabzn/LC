https://leetcode.com/problems/maximal-score-after-applying-k-operations/

class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        score = 0
        heap = []
        for num in nums:
            heappush(heap, -num)
        
        for _ in range(k):
            num = -heappop(heap)
            score += num
            heappush(heap, -int(ceil(num / 3)))
            
        return score
