https://leetcode.com/problems/encode-and-decode-strings/
  
class Codec:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ''
        """
        Get the length of each str and encode it with its length on the front
        Separate its length and the str with a ! to indicate its length .
        
        [Hello, World] -> 5!Hello5!World
        """
        for s in strs:
            LEN = len(s)
            encoded_str = encoded_str + str(LEN) + '!' + s
        
        return encoded_str

    def decode(self, s: str) -> List[str]:
        decoded_strs = []
        index, LEN = 0, len(s)
        
        while index < LEN:
            cur_len, cur_str = '', ''
            seen_delimeter = False
            
            while not seen_delimeter:
                cur_char = s[index]
                if cur_char == '!':
                    seen_delimeter = True
                else:
                    cur_len = cur_len + cur_char
                index += 1
                 
            cur_len = int(cur_len)
            while cur_len:
                cur_str = cur_str + s[index]
                cur_len -= 1
                index += 1
            
            decoded_strs.append(cur_str)
        return decoded_strs
