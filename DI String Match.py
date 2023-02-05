I have no idea what this problem is about...
I don't even know how I come up with the solution...

https://leetcode.com/problems/di-string-match/
class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        res = [None] * (len(s))
        i, d = 0, len(s)
        visited_nums = set()
        
        for idx, char in enumerate(s):
            if char == 'I':
                res[idx] = i
                visited_nums.add(i)
                i += 1
            else:
                res[idx] = d
                visited_nums.add(d)
                d -= 1
        
        for i in range(len(s) + 1):
            if i not in visited_nums:
                res.append(i)
        
        return res
