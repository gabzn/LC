https://leetcode.com/problems/all-paths-from-source-to-target/
  
from collections import deque

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        target = len(graph) - 1
        
        res, path = [], [0]
        queue = deque()
        queue.append(path)
        
        # Use BFS to do this one.
        while queue:
            cur_path = queue.popleft()
            
            # cur_path is a list of values from node 0 to its neighbours
            # Every time we popped from the queue, we want to check if the rightmost val is equal to the target
            # If it is, just append this path to the res and go to the next iteration.
            rightmost_val = cur_path[-1]
            if rightmost_val == target:
                res.append(cur_path)
                continue
            
            # If it gets here, that means the rightmost node wasn't the target.
            # We append more children into the current path.
            for neighbour in graph[rightmost_val]:
                # new_list = []
                # for node in cur_path:
                #     new_list.append(node)
                # new_list.append(neighbour)
                
                cur_path.append(neighbour)
                queue.append(cur_path.copy())
                cur_path.pop()
            
        return res
