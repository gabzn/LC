https://leetcode.com/problems/distribute-elements-into-two-arrays-ii/

from sortedcontainers import SortedList

class Solution:
    def resultArray(self, nums: List[int]) -> List[int]:
        def greater_count(arr, num):
            return len(arr) - arr.bisect_right(num)
        
        def insert(sorted_lst, lst, num):
            sorted_lst.add(num)
            lst.append(num)
        
        N = len(nums)

        a = [nums[0]]
        b = [nums[1]]
        arr1_sorted = SortedList(a)
        arr2_sorted = SortedList(b)

        for i in range(2, N):
            num = nums[i]
            o1 = greater_count(arr1_sorted, num)
            o2 = greater_count(arr2_sorted, num)
            
            if o1 > o2 or (o1 == o2 and len(arr1_sorted) <= len(arr2_sorted)):
                insert(arr1_sorted, a, num)
                continue
                
            if o1 < o2 or (o1 == o2 and len(arr1_sorted) > len(arr2_sorted)):
                insert(arr2_sorted, b, num)

        return a + b
