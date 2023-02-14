https://leetcode.com/problems/find-the-k-beauty-of-a-number/
  
class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        str_num = str(num)
        l, res = 0, 0
        
        for r in range(k-1, len(str_num)):
            substr = int(str_num[l: r+1])
            
            if substr and num % substr == 0:
                res += 1
            
            l += 1

        return res
