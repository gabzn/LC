https://leetcode.com/problems/find-smallest-letter-greater-than-target/
  
You are given an array of characters letters that is sorted in non-decreasing order, and a character target. There are at least two different characters in letters.

Return the smallest character in letters that is lexicographically greater than target. If such a character does not exist, return the first character in letters.

class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        l, r = 0, len(letters) - 1
        target_in_int = ord(target)
        
        while l <= r:
            m = (l + r) // 2
            
            middle_letter_in_int = ord(letters[m])
            if middle_letter_in_int > target_in_int:
                r = m - 1
            else:
                l = m + 1
            
        return letters[ l % len(letters) ]
