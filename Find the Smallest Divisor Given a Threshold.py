https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/

class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        left, right = 0, 10 ** 6
        
        while left + 1 != right:
            mid = (left + right) // 2
            
            if threshold >= sum([math.ceil(num / mid) for num in nums]):
                right = mid
            else:
                left = mid
        
        return right
