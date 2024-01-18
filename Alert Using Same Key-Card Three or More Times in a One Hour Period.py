https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

class Solution:
    def alertNames(self, names: List[str], times: List[str]) -> List[str]:
        def change_time_format(t: str):
            return int(t.replace(':', ''))
        
        names_and_times = []
        for name, time in zip(names, times):
            names_and_times.append((name, change_time_format(time)))
        names_and_times.sort()
        
        res = []
        is_sus = set()
        access = defaultdict(deque)
         
        for name, time in names_and_times:
            if name not in access:
                access[name].append(time)
            else:
                while len(access[name]) > 0 and time - access[name][0] > 100:
                    access[name].popleft()
                
                access[name].append(time)
                if len(access[name]) >= 3 and name not in is_sus:
                    res.append(name)
                    is_sus.add(name)
            
        return res
