https://leetcode.com/problems/time-based-key-value-store/
  
class TimeMap:

    def __init__(self):
        self.time_map = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.time_map[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map:
            return ''
        
        values = self.time_map[key]
        if timestamp < values[0][0]:
            return ''
        
        l, r = -1, len(values)
        while l + 1 != r:
            m = (l + r) // 2
            m_timestamp = values[m][0]
  
            if timestamp >= m_timestamp:
                l = m
            else:
                r = m 
        
        return values[l][1]
