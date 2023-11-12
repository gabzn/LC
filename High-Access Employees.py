https://leetcode.com/problems/high-access-employees/

class Solution:
    def findHighAccessEmployees(self, access_times: List[List[str]]) -> List[str]:
        LEN = len(access_times)
            
        for i in range(LEN):
            access_times[i][1] = int(access_times[i][1])
        
        access_times.sort(key=lambda t: (t[0], t[1]))
        
        res = set()
        access = defaultdict(deque)
        for name, t in access_times:
            if name not in access:
                access[name].append(t)
            else:
                while len(access[name]) > 0 and t - access[name][0] >= 100:
                    access[name].popleft()
                
                access[name].append(t)
                if len(access[name]) >= 3:
                    res.add(name)
                    
        return res
