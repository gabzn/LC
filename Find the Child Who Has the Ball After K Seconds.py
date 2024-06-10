https://leetcode.com/problems/find-the-n-th-value-after-k-seconds/

class Solution:
    def numberOfChild(self, n: int, k: int) -> int:
        i = 0
        to_right = True
        while k:
            if to_right:
                i += 1
                if i == n - 1:
                    to_right = False
            else:
                i -= 1
                if i == 0:
                    to_right = True

            k -= 1
        return i
