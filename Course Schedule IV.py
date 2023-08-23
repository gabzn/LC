https://leetcode.com/problems/course-schedule-iv/

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:        
        reachable = [set() for _ in range(numCourses)]
        res = []
        
        # Build the graph and degree list
        graph = defaultdict(list)
        indegrees = [0] * numCourses
        for a, b in prerequisites:
            graph[a].append(b)
            indegrees[b] += 1
        
        # Push courses that have no prerequisites to the queue
        queue = deque()
        for course, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(course)
        
        while queue:
            preq = queue.popleft()
            
            for sub in graph[preq]:
                
                # The prerequisites of preq are also the prerequisites of sub
                for prerequisites_of_preq in reachable[preq]:
                    reachable[sub].add(prerequisites_of_preq)
                
                # preq is a prerequisite of sub 
                reachable[sub].add(preq)
                
                indegrees[sub] -= 1                
                if indegrees[sub] == 0:
                    queue.append(sub)
        
        for u, v in queries:
            if u in reachable[v]:
                res.append(True)
            else:
                res.append(False)
         
        return res
