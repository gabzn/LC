https://leetcode.com/problems/minimum-index-of-a-valid-split/

class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        N = len(nums)

        total_counter = Counter(nums)
        right, right_count = total_counter.most_common(1)[0]
        left_count = 0
        
        for i, left in enumerate(nums):
            if left == right:
                left_count += 1
                right_count -= 1
                
                if left_count * 2 > (i + 1) and right_count * 2 > N - i - 1:
                    return i
         
        return -1
