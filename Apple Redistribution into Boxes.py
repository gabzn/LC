https://leetcode.com/problems/apple-redistribution-into-boxes/

class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:        
        apples = sum(apple)
        capacity.sort(reverse=True)
        res = idx = 0
        
        while apples:
            apples = max(apples - capacity[idx], 0)
            idx += 1
            res += 1
            
        return res
