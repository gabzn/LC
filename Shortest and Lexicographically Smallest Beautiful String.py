https://leetcode.com/problems/shortest-and-lexicographically-smallest-beautiful-string/

class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        LEN = len(s)
        s_lst = [char for char in s]
        
        pref = [0]
        for char in s_lst:
            if int(char) == 1:
                pref.append(pref[-1] + 1)
            else:
                pref.append(pref[-1])
        
        shortest = LEN
        res = ''
        
        for right in range(LEN + 1):
            if pref[right] >= k:
                diff = pref[right] - k
                
                left = right
                while left >= 0:
                    if pref[left] == diff:
                        break
                    left -= 1
                
                if (right - left) <= shortest:
                    temp = ''.join(s_lst[left: right])
                    
                    if not res or res > temp or right - left < shortest:
                        res = temp
                        
                    shortest = min(right - left, shortest)
                    
        return res
