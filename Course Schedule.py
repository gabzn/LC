https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue = deque()
        indegrees = [0] * numCourses
        graph = defaultdict(list)
        courses_taken = 0
        
        # Make a graph where preq is the key and courses that depend on preq as its values
        for course, preq_of_course in prerequisites:
            graph[preq_of_course].append(course)
            indegrees[course] += 1
        
        # Append the starter courses to the queue
        # Starter courses are either the preq of other courses or just standalone courses
        for course_num, degree in enumerate(indegrees):
            if degree == 0:
                queue.append(course_num)        
        
        while queue:
            preq_course = queue.popleft()
            courses_taken += 1
            
            for course in graph[preq_course]:
                indegrees[course] -= 1
                if indegrees[course] == 0:
                    queue.append(course)
        
        return courses_taken == numCourses
