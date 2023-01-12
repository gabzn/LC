https://leetcode.com/problems/generate-parentheses/

# Very similar to letter combinations of a phone number
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        if not n:
            return []
        
        return self.generate(n, 0, 0, '', [])
    
    def generate(self, n, left, right, current, res):
        if left == n and right == n:
            res.append(current)
            return res
        
        if left < n:
            res = self.generate(n, left + 1, right, current + '(', res)
        
        if right < left:
            res = self.generate(n, left, right + 1, current + ')', res)
            
        return res
