https://leetcode.com/problems/longest-repeating-character-replacement/

You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. 
You can perform this operation at most k times.

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if len(s) == 1:
            return 1
        
        l, r, max_length, max_num_of_repeating_char = 0, 0, 0, 0
        char_count_list = [0] * 26
        
        for char in s:
            # Find the char index and increment the count of this char in the list
            char_index = ord(char) - ord('A')
            char_count_list[char_index] += 1
            
            # Every time the count of a char is incremented, check to see if it's the leading repeated char
            max_num_of_repeating_char = max(max_num_of_repeating_char, char_count_list[char_index])
            
            # Find the number of character to replace by subtracting the count of the repeating char from the length of the current window
            #                    The length of the current window -> r - l + 1
            # If: the number of char needed to be replaced is <= the total number of replacement k, update the max_length
            # Else: move the left pointer 1 unit to the right but before that, decrement the count of the char l is currently looking at
            num_of_char_to_replace = (r - l + 1) - max_num_of_repeating_char
            if num_of_char_to_replace <= k:
                max_length = (r - l + 1)
            else:
                char_count_list[ord(s[l]) - ord('A')] -= 1
                l += 1
            
            r += 1
            
        return max_length
