https://leetcode.com/problems/intersection-of-two-arrays-ii/

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counter1 = Counter(nums1)
        counter2 = Counter(nums2)

        res = []

        for num in counter1:
            for _ in range(min(counter1[num], counter2[num])):
                res.append(num)

        return res
