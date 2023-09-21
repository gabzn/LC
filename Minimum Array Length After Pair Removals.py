https://leetcode.com/problems/minimum-array-length-after-pair-removals/

class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        LEN = len(nums)
        
        length = LEN
        mid = length // 2
        
        i, j = 0, (LEN + 1) // 2
        while i < mid and j < LEN:
            if nums[i] < nums[j]:
                length -= 2
            
            i += 1
            j += 1
    
        return length
-------------------------------------------------------------------------------
class Solution:
    def minLengthAfterRemovals(self, nums: List[int]) -> int:
        length = len(nums)
        
        counter = Counter(nums)
        heap = [(-count, num) for num, count in counter.items()]
        heapify(heap)
        
        while len(heap) >= 2:
            first_freq, n1 = heappop(heap)
            second_freq, n2 = heappop(heap)
            
            first_freq *= -1
            second_freq *= -1
            
            first_freq -= 1
            second_freq -= 1
            length -= 2
            
            if first_freq:
                heappush(heap, (-first_freq, n1))
            if second_freq:
                heappush(heap, (-second_freq, n2))
            
            
        return length
