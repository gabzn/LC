https://leetcode.com/problems/find-the-prefix-common-array-of-two-arrays/

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        N = len(A)
        res = [0] * N
        a_set = set()
        b_set = set()
        for i in range(N):
            a = A[i]
            b = B[i]
            x = 1 if a == b else 0
            if a in b_set:
                x += 1
            if b in a_set:
                x += 1
            res[i] = res[i - 1] + x
            a_set.add(a)
            b_set.add(b)
        return res
