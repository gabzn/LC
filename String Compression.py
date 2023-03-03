https://leetcode.com/problems/string-compression/
  
class Solution:
    def compress(self, chars: List[str]) -> int:
        l, same_char_count, idx = 0, 0, 0
        
        while l < len(chars):
            r = l
            while r < len(chars) and chars[l] == chars[r]:
                r += 1
                same_char_count += 1
            
            """
            a a a a a a b b
            a 6 a a a a b b     idx = 2
            [a 6 b 2] a a b b   idx = 5
            we use idx for 2 purposes, one is to place the char and the other is to place the digits
            """
            chars[idx] = chars[l]
            idx += 1
            
            if same_char_count > 1:
                count_str = str(same_char_count)
                for char in count_str:
                    chars[idx] = char
                    idx += 1
            
            same_char_count = 0     # Reset the count to 0
            l = r                   # Move l to r
        
        # print(chars, idx)
        return idx
