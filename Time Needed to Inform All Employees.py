https://leetcode.com/problems/time-needed-to-inform-all-employees/

class Solution:
    def numOfMinutes(self, n: int, root_id: int, manager: List[int], time_needed_to_inform_workers: List[int]) -> int:
        graph = defaultdict(list)
        for employee_id in range(n):
            if employee_id == root_id:
                continue
            manager_id = manager[employee_id]
            graph[manager_id].append((employee_id, time_needed_to_inform_workers[manager_id]))
        
        total_time = 0
        
        queue = deque([(root_id, 0)])
        while queue:
            employee_id, time = queue.popleft()
            total_time = max(total_time, time)    
            
            for subordinate, t in graph[employee_id]:
                queue.append((subordinate, t + time))
                            
        return total_time
