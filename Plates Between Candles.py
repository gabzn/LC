https://leetcode.com/problems/plates-between-candles/

class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:        
        N = len(s)
        
        pref = []
        running_sum = 0
        for idx in range(N):
            running_sum += (s[idx] == '*')
            pref.append(running_sum)
                    
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
------------------------------------------------------------------------------------------------
class Solution:
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:        
        def get_plates(left, right):            
            if s[left] == s[right] == '|':
                return pref[right] - pref[left]
            
            if s[left] == '|':
                right = bisect_left(candle_indices, right) - 1           
                if left <= candle_indices[right]:
                    return pref[candle_indices[right]] - pref[left]
                return 0
            
            if s[right] == '|':
                left = bisect_right(candle_indices, left)
                if candle_indices[left] <= right:
                    return pref[right] - pref[candle_indices[left]]
                return 0                
            
            left = bisect_right(candle_indices, left)
            right = bisect_left(candle_indices, right) - 1
            if left <= right:
                return pref[candle_indices[right]] - pref[candle_indices[left]]
            return 0
        
        N = len(s)
        
        pref = []
        running_sum = 0
        for idx in range(N):
            running_sum += (s[idx] == '*')
            pref.append(running_sum)
        
        candle_indices = [idx for idx, char in enumerate(s) if char == '|']
        return [get_plates(left, right) for left, right in queries]
