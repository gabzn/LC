https://leetcode.com/problems/longest-common-prefix/
  
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".

Input: strs = ["flower","flow","flight"]
Output: "fl"
  
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        
        prefix = ''     
        index = 0
        
        """
        Build the prefix based on the first str in strs
        Take each char in the first str and compare it with the other strs to see if the char is the same.
        Use index to move the char we want to check in other strs.
        The longest substring is ALWAYS constrained by the shortest string in strs.
        """
        for char in strs[0]:
            for s in range(1, len(strs)):
                cur_str = strs[s]
                
                if index > len(cur_str)-1 or char != cur_str[index]:
                    return prefix
                
            prefix += char
            index += 1
                
        return prefix
