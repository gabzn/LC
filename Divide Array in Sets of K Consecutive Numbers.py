https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/

class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        N = len(nums)
        
        if N % k > 0:
            return False
        
        counter = Counter(nums)
        heap = list(counter.keys())
        heapify(heap)
        
        while heap:
            start = heap[0]
            
            for x in range(start, start + k):
                if x not in counter:
                    return False
                
                counter[x] -= 1
                if counter[x] == 0:
                    if x != heap[0]:
                        return False
                    heappop(heap)
        
        return True
