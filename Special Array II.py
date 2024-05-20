https://leetcode.com/problems/special-array-ii/

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        lst = []
        for x, y in pairwise(nums):
            if x % 2 == y % 2:
                lst.append(1)
            else:
                lst.append(0)
        
        pref = [0]
        for x in lst:
            pref.append(pref[-1])
            pref[-1] += x
                         
        return [pref[t] - pref[s] == 0 for s, t in queries]
