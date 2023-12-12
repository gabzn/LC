https://leetcode.com/problems/divide-chocolate/

class Solution:
    def maximizeSweetness(self, sweetness: List[int], k: int) -> int:
        def can_split_all_into_at_least_mid_sweetness(mid):
            cur_sweetness = chunks = 0
            
            for s in sweetness:
                cur_sweetness += s
                if cur_sweetness >= mid:
                    chunks += 1
                    cur_sweetness = 0
            
            return chunks >= k + 1
        
        left, right = 0, 10 ** 10
            
        while left + 1 != right:
            mid = (left + right) // 2
            
            if can_split_all_into_at_least_mid_sweetness(mid):
                left = mid
            else:
                right = mid
    
        return left
