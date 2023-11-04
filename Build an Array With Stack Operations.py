https://leetcode.com/problems/build-an-array-with-stack-operations/

class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        LEN = len(target)
        
        nums_in_stack = 0
        res = []
            
        for num in range(1, n + 1):
            if num not in target:
                if nums_in_stack < LEN:
                    res.append('Push')
                    res.append('Pop')
            else:
                res.append('Push')
                nums_in_stack += 1
            
        return res
