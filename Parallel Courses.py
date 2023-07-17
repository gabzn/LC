https://leetcode.com/problems/parallel-courses/

class Solution:
    def minimumSemesters(self, n: int, relations: List[List[int]]) -> int:
        indegrees = [0] * (n + 1)
        adj_list = defaultdict(list)
        queue = deque()
        min_semesters, courses_taken = 0, 0
        
        for preq_course, next_course in relations:
            adj_list[preq_course].append(next_course)
            indegrees[next_course] += 1
        
        for course_num in range(1, n + 1):
            if indegrees[course_num] == 0:
                queue.append((course_num, 1))
                
        while queue:
            course_num, semester = queue.popleft()
            courses_taken += 1
            min_semesters = semester
            
            for next_course in adj_list[course_num]:
                indegrees[next_course] -= 1
                if indegrees[next_course] == 0:
                    queue.append((next_course, semester + 1))
        
        return min_semesters if courses_taken == n else - 1
