https://leetcode.com/problems/relative-sort-array/

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        N = len(arr1)
        M = len(arr2)
        
        ordering = {i: num for i, num in enumerate(arr2)}
        counter = Counter(arr1)
        i = j = 0
        
        while j < M:
            num = ordering[j]
            
            while counter[num]:
                arr1[i] = num
                counter[num] -= 1
                i += 1
            
            j += 1
            del counter[num]
        
        remaining = sorted(counter.items(), reverse=True)
        
        while i < N:
            num, freq = remaining.pop()
            
            while freq:
                arr1[i] = num
                i += 1
                freq -= 1
        
        return arr1
