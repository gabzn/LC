https://leetcode.com/problems/process-tasks-using-servers/

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:        
        busy = []
        free = [(w, i) for i, w in enumerate(servers)]
        heapify(free)
        
        res = []
        for task_index, task_time in enumerate(tasks):
            while busy and busy[0][0] <= task_index:
                _, w, i = heappop(busy)
                heappush(free, (w, i))
            
            if free:
                w, i = heappop(free)
                heappush(busy, (task_index + task_time, w, i))
                res.append(i)
            else:
                last_finish_time, w, i = heappop(busy)
                heappush(busy, (last_finish_time + task_time, w, i))
                res.append(i)

        return res
--------------------------------------------------------------------------------
class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        ans, busy_servers, free_servers = [], [], []

        for index in range(len(servers)):
            heappush(free_servers, (servers[index], index))
            
        # busy_servers = ( finishing_time, weight, server_index )
        # free_servers = ( weight, server_index )
        for task_index, duration in enumerate(tasks):
            # Free the servers that become available when we process the current task.
            while busy_servers and task_index >= busy_servers[0][0]:
                _, weight, server_index = heappop(busy_servers)
                heappush(free_servers, (weight, server_index))
            
            # If there's servers available to process the task,
            # pull the first server out from the free heap and compute its end time,
            # and put this server into the busy heap.
            if free_servers:
                weight, server_index = heappop(free_servers)  
                ans.append(server_index)  
                
                end_time = task_index + duration
                heappush(busy_servers, (end_time, weight, server_index))
            # Else there's no servers available, we look at the next available server in the busy heap.
            # Pull it out and assign the current task to it,
            # and put it back to the busy heap becasue we immediately use this server to process the task.
            else:
                end_time, weight, server_index = heappop(busy_servers)
                ans.append(server_index)
                
                end_time += duration
                heappush(busy_servers, (end_time, weight, server_index))
                        
        return ans
