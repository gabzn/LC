https://leetcode.com/problems/course-schedule-ii/

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        queue = deque()
        graph = defaultdict(list)
        ordering, indegrees = [], [0] * numCourses
        
        for course, preq_of_course in prerequisites:
            graph[preq_of_course].append(course)
            indegrees[course] += 1
        
        for course, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(course)
                
        while queue:
            preq_course = queue.popleft()
            ordering.append(preq_course)
            
            for course in graph[preq_course]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        
        return ordering if len(ordering) == numCourses else []
