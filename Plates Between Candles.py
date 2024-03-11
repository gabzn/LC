https://leetcode.com/problems/plates-between-candles/

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:        
        N = len(s)
        
        one_flag = False if s[0] == '*' else True
        pref = [0]
        for idx in range(1, len(s)):
            if one_flag:
                if s[idx] == '*':
                    pref.append(pref[-1] + 1)
                else:
                    pref.append(pref[-1])
            else:
                if s[idx] == '|':
                    one_flag = True
                pref.append(0)
        
        closest_candle_to_the_left_of_i = []
        closest_candle = -1
        for i in range(N):
            if s[i] == '|':
                closest_candle = i
            closest_candle_to_the_left_of_i.append(closest_candle)

        closest_candle_to_the_right_of_i = []
        closest_candle = N
        for i in range(N - 1, -1, -1):
            if s[i] == '|':
                closest_candle = i
            closest_candle_to_the_right_of_i.append(closest_candle)
        closest_candle_to_the_right_of_i.reverse()
                
        res = []
        for a, b in queries:
            left = closest_candle_to_the_right_of_i[a]
            right = closest_candle_to_the_left_of_i[b]
            
            if left > right:
                res.append(0)
            else:
                res.append(pref[right] - pref[left])
        
        return res
