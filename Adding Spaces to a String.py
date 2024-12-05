https://leetcode.com/problems/adding-spaces-to-a-string/

class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = []
        space_i = 0
        for i, char in enumerate(s):
            if space_i < len(spaces) and spaces[space_i] == i:
                res.append(' ')
                space_i += 1
            res.append(char)
        return ''.join(res)
