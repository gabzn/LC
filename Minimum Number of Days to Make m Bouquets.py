https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/

class Solution:
    def minDays(self, bloom_days: List[int], m: int, k: int) -> int:
        def can_make_m_bouquets_in_mid_days(mid):
            bouquets_count = flowers_used = 0
            
            for day in bloom_days:
                if day > mid:
                    flowers_used = 0
                else:
                    flowers_used += 1
                    if flowers_used == k:
                        bouquets_count += 1
                        flowers_used = 0
            
            return bouquets_count >= m
         
        if m * k > len(bloom_days):
            return -1
        
        left, right = 0, 10 ** 9 + 1
        while left + 1 != right:
            mid = (left + right) // 2
            
            if can_make_m_bouquets_in_mid_days(mid):
                right = mid
            else:
                left = mid
        
        return right
