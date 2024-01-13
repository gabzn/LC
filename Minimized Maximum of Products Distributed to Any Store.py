https://leetcode.com/problems/minimized-maximum-of-products-distributed-to-any-store/

class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        def find_num_stores_needed_to_distribute_at_most_m(m):
            num_stores = 0
            
            for amount in quantities:
                num_stores += ceil(amount / m)            
            
            return num_stores
        
        l, r = 0, max(quantities) + 1
   
        while l + 1 != r:
            m = (l + r) // 2
            
            stores_needed = find_num_stores_needed_to_distribute_at_most_m(m)
            
            # If we need more stores than we have when we are distributing at most m products,
            # we increase m to get fewer or equal stores
            if stores_needed > n:
                l = m
            else:
                r = m
                
        return r
