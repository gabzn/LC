https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        graph = defaultdict(list)
        for employee_id in range(n):
            if employee_id == headID:
                continue
            manager_id = manager[employee_id]
            graph[manager_id].append((employee_id, informTime[manager_id]))
        
        total_time = 0
        
        queue = deque([(headID, 0)])
        while queue:
            employee_id, time = queue.popleft()
            total_time = max(total_time, time)    
            
            for subordinate, t in graph[employee_id]:
                queue.append((subordinate, t + time))
                            
        return total_time
