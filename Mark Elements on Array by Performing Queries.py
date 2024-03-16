https://leetcode.com/problems/mark-elements-on-array-by-performing-queries/

class Solution:
    def unmarkedSumArray(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        N = len(nums)
        
        remaining = sum(nums)
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapify(heap)
        
        is_marked = [False] * N
        
        res = []
        for idx, k in queries:
            val = 0
            
            if not is_marked[idx]:
                is_marked[idx] = True
                val += nums[idx]
            
            while heap and k:
                num, i = heappop(heap)
                if is_marked[i]:
                    continue
                
                is_marked[i] = True
                val += num
                    
                k -= 1
                        
            remaining -= val
            res.append(remaining)    
        
        return res
